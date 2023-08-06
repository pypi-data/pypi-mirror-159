#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from datetime import datetime

import click

from sagemaker.processing import ProcessingInput, ProcessingOutput

from ..aws.processing import get_sklearn_processor
from ..aws.s3 import download_s3_directory, get_s3_resource
from ..config import read_yaml
from ..constants import SAGEMAKER_CONTAINER_PATH_MAIN
from ..log import get_logger, verbosity_option
from ..utils.zip import zip_directory
from . import rudderlabs

logger = get_logger(__name__)


def run_pipeline_step(
    pipeline: dict,
    creds: dict,
    repo_zip_path: str,
    instance_type: str,
    job_id: str,
    repository_path: str,
) -> None:
    """Runs given pipeline step in sci-kit learn processor in amazon sagemaker

    Args:
        pipeline: Pipeline step information
        creds: AWS credentials
        repo_zip_path: Compressed repository path
        instance_type: Instance type to use for the sagemaker job
        job_id: all the outputs will be saved under the folder with this name
        repository_path: Path to the repository

    Returns:
        None: None
    """
    # Get sklearn processor
    logger.info(f"Pipeline step: {pipeline['name']}")
    job_name = f"{pipeline['name']}-{pipeline['job_suffix']}"
    sklearn_processor = get_sklearn_processor(creds, instance_type, job_name)

    sagemaker_code_path = os.path.join(SAGEMAKER_CONTAINER_PATH_MAIN, "code")
    sagemaker_req_path = os.path.join(
        SAGEMAKER_CONTAINER_PATH_MAIN, "requirements"
    )
    output_path = os.path.join(SAGEMAKER_CONTAINER_PATH_MAIN, "output")

    local_req_path = os.path.join(repository_path, "requirements.txt")

    params = {f"{k}": v for k, v in pipeline["params"].items()}

    # Pass job id to the pipeline script as a parameter
    params["--input-code-path"] = os.path.join(
        SAGEMAKER_CONTAINER_PATH_MAIN, "input", "code"
    )
    params["--requirements-path"] = os.path.join(
        sagemaker_req_path, "requirements.txt"
    )
    params["--code-zip-path"] = os.path.join(
        sagemaker_code_path, os.path.basename(repo_zip_path)
    )
    params["--output-path"] = output_path
    params["--job-id"] = job_id
    arguments = []
    for k, v in params.items():
        arguments.append(f"{k}")
        arguments.append(f"{v}")

    logger.info(f"Arguments: {arguments}")

    sklearn_processor.run(
        code=pipeline["code"],
        inputs=[
            ProcessingInput(
                source=repo_zip_path, destination=sagemaker_code_path
            ),
            ProcessingInput(
                source=local_req_path, destination=sagemaker_req_path
            ),
        ],
        outputs=[ProcessingOutput(source=output_path)],
        arguments=arguments,
    )

    if instance_type != "local":
        # Downloading model output files into local
        s3_resource = get_s3_resource(creds)
        s3_bucket = creds["s3Bucket"]
        process_job_output_path = (
            f"{sklearn_processor.latest_job.job_name}/output/output-1/{job_id}"
        )
        local_output_path = os.path.join(
            repository_path, pipeline["output_path"], job_id
        )

        download_s3_directory(
            s3_resource, s3_bucket, process_job_output_path, local_output_path
        )

    else:
        print(
            "Processor ran locally. Download files from docker container to data/ before moving ahead to the next step."
        )
        """
        Can be done by doing following steps from console:
        > docker container ls -a
        This gives the list of containers. Get the latest container id.
        Then copy the exact file and use the id as follows:
        > docker cp 1a28de8ebcf5://opt/ml/processing/output/filename .      # This will download the output folder contents to the current directory.
        If this doesnt work, try starting the container and then copy the file
        > docker container start <container_id>
        > docker cp <container_id>://opt/ml/processing/output/filename .
        """


@click.command(
    epilog="""
    The command to run given notebookes in the pipeline.

    Examples:

        $ rlabs aws run-pipeline --pipeline-file pipeline.yaml --credentials-file credentials.yaml --repository-path /path/to/repository --instance-type ml.t3.xlarge --job-id my-job-id

        $ rlabs aws run-pipeline -p pipeline.yaml -c credentials.yaml -r /path/to/repository -i local -j my-job-id
    """
)
@click.option(
    "-j",
    "--job-id",
    default=None,
    help="Job id to be used for the pipeline, used to store output files in S3/local",
)
@click.option(
    "-c",
    "--credentials-file",
    type=click.Path(exists=True, readable=True, resolve_path=True),
    show_default=True,
    default=os.path.join(os.path.realpath(os.curdir), "credentials.yaml"),
)
@click.option(
    "-i",
    "--instance-type",
    default="ml.t3.xlarge",
    show_default=True,
    help="The instance type to use for the amazon sagemaker notebook instance.",
)
@click.option(
    "-p",
    "--pipeline-config-file",
    type=click.Path(exists=True, readable=True, resolve_path=True),
    help="The pipeline config file to use.",
)
@click.option(
    "-r",
    "--repository-path",
    default=os.path.realpath(os.curdir),
    show_default=True,
    type=click.Path(exists=True, readable=True, resolve_path=True),
    help="The repository path to use.",
)
@verbosity_option()
@rudderlabs.raise_on_error
def run_pipeline(
    job_id: str,
    credentials_file: click.Path,
    instance_type: str,
    pipeline_config_file: click.Path,
    repository_path: click.Path,
) -> None:

    logger.info("Running pipeline")
    logger.info("credentials_file: %s", credentials_file)
    logger.info("Instance type: %s", instance_type)

    if job_id is None:
        job_id = int(datetime.now().timestamp())

    # Load the pipeline config file
    pipeline_config = read_yaml(pipeline_config_file)
    logger.info("Pipeline config: %s", pipeline_config)

    # Load the credentials file
    config = read_yaml(credentials_file)
    repo_zip_path = zip_directory(repository_path)

    # Runing pipeline
    for pipeline_step in pipeline_config["pipeline"]:
        logger.info("Running pipeline step: %s", pipeline_step["name"])

        run_pipeline_step(
            pipeline_step,
            config,
            repo_zip_path,
            instance_type,
            job_id,
            repository_path,
        )
