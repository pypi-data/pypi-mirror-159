#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess
import sys

from pathlib import Path

import click


@click.command(
    epilog="""
    Script for running a notebook in a sagemaker job.

    Example:

        $ rudderlabs run_notebook_wrapper --notebook_path ./notebooks/notebook.ipynb --params {"param1": "value1", "param2": "value2"}
    """
)
# These manditory options for every script
@click.option(
    "-i",
    "--input-code-path",
    required=True,
    type=click.Path(exists=True),
    help="Path to the source code directory",
)
@click.option(
    "-r",
    "--requirements-path",
    required=True,
    type=click.Path(exists=True),
    help="Path to the requirements.txt file",
)
@click.option(
    "-c",
    "--code-zip-path",
    required=True,
    type=click.STRING,
    help="Path to the code zip file",
)
@click.option(
    "-o",
    "--output-path",
    required=True,
    type=click.Path(exists=True),
    help="Path to the output directory",
)
@click.option(
    "-j",
    "--job-id",
    required=True,
    type=click.STRING,
    help="Job id to be passed to notebook execution script",
)
# These are optional parameters specific to this script, and these parameters will come from
# the pipeline config
# Example:(content of sample pipeline)
# pipeline:
#  - name: "sample_step"
#    job_suffix: "S"
#    code: "run_notebook_wrapper.py"
#    output_path: "data"
#    params:
#      notebook_path: "notebook/sample_notebook.ipynb"
#      train_id: "1"
#
#
#   While running above "sample_step" using this script the optional params will be
# --notebook_path "notebook/sample_notebook.ipynb" --train_id "1"
#
#  Specify the optoins in accordance with the pipeline config
@click.option(
    "-n",
    "--notebook-path",
    required=True,
    type=click.Path(exists=False),
    help="Path to the notebook to be executed",
)
@click.option(
    "-t",
    "--train-id",
    default=0,
    required=False,
    type=click.INT,
    help="Train id to be passed to notebook execution script",
)
def notebook_run_script(
    input_code_path: click.Path,
    requirements_path: click.STRING,
    code_zip_path: click.Path,
    output_path: click.Path,
    job_id: click.STRING,
    notebook_path: click.Path,
    train_id: click.INT,
) -> None:
    # First install requirements so that rudderlabs/data/apps/templates/notebook_execution_script.py can be run
    # It is expected that the requirements are already there in the sagemaker container path
    print("Params:")
    print("input_code_path: {}".format(input_code_path))
    print("requirements_path: {}".format(requirements_path))
    print("code_zip_path: {}".format(code_zip_path))
    print("output_path: {}".format(output_path))
    print("job_id: {}".format(job_id))
    print("notebook_path: {}".format(notebook_path))
    print("train_id: {}".format(train_id))
    print("")

    subprocess.run(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "-r",
            requirements_path,
            "--quiet",
        ]
    )

    # Unzip the code zip file
    from rudderlabs.data.apps.log import setup_file_logger
    from rudderlabs.data.apps.utils import list_files
    from rudderlabs.data.apps.utils.notebook import (
        get_html_from_notebook,
        run_notebook,
    )
    from rudderlabs.data.apps.utils.zip import unzip_directory

    logfile_name = os.path.splitext(os.path.basename(__file__))[0] + ".log"
    logfile_path = os.path.join(output_path, "logs", logfile_name)
    if not os.path.exists(logfile_path):
        os.makedirs(os.path.dirname(logfile_path))

    logger = setup_file_logger(logfile_path)

    logger.info("Unzipping code zip file")
    unzip_directory(code_zip_path, input_code_path)
    list_files(input_code_path)

    nb_params = {
        "train_id": train_id,
        "run_id": job_id,
        "code_path": input_code_path,
        "local_output_path": output_path,
    }

    logger.info("Running notebook")
    logger.info(
        f"Notebook path: {os.path.join(input_code_path, notebook_path)}"
    )
    logger.info(f"Notebook params: {nb_params}")

    abs_notebook_path = os.path.join(input_code_path, notebook_path)
    print(abs_notebook_path)
    output_notebook_path = run_notebook(abs_notebook_path, nb_params)
    html_path = get_html_from_notebook(output_notebook_path)

    Path(output_path).mkdir(parents=True, exist_ok=True)

    # Copy html file to output path
    subprocess.run(
        f"mv {html_path} {os.path.join(output_path, os.path.basename(html_path))}".split()
    )


if __name__ == "__main__":
    notebook_run_script()
