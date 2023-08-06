"""Supporting utilities.
"""
import json
import os
from dataclasses import dataclass
from pathlib import Path
# from typing import Any, Optional, Sequence, Union
#
# from aws_cdk import App as _App
# from aws_cdk import aws_s3 as s3
# from aws_cdk import aws_s3_deployment as s3_deploy
# from aws_cdk.region_info import RegionInfo
# from checksumdir import dirhash
from pkg_resources import get_distribution
from pippy_ls.custom_errors import CDKVersionError


ROOT_PATH = str(Path(".").resolve())


@dataclass
class DeployEnv:
    name: str
    stage: str
    index_alias: str
    index_model: str
    index_dataset: str


def check_cdk_version(pkg: str = "aws-cdk-lib", cfg: str = "pyproject.toml"):
    installed_cdk_version = get_distribution(pkg).version
    desired_version = ""
    with open(f"{ROOT_PATH}/{cfg}", "r") as setup_file:
        lines = setup_file.readlines()
        for line in lines:
            if line.startswith(pkg):
                # handle semver checking
                check = line.split("=")[1].strip().strip('"')
                if check[0] == "~" or check[0] == "^":
                    desired_version = check[1:]
                elif check[0] == ">" or check[0] == "<":
                    desired_version = check[2:]
                else:
                    desired_version = check

    print(f'installed_cdk_version: {installed_cdk_version}')
    print(f'desired_version: {desired_version}')
    if installed_cdk_version != desired_version:
        raise CDKVersionError(installed_cdk_version, desired_version)


