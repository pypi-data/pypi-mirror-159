"""Base-classes for Lambda Function and Layer to operate in commercial and Iso regions.
"""

from os import fspath
from pathlib import Path as _Path
from typing import Optional, Sequence, Union

from aws_cdk import BundlingOptions, DockerVolume, RemovalPolicy, Stack
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_sqs as sqs
from aws_cdk.aws_iam import AnyPrincipal, Effect, PolicyStatement
from aws_cdk.aws_iam import Role as _Role
from aws_cdk.aws_logs import RetentionDays
from constructs import Construct


class DefaultBucket(s3.Bucket):
    def __init__(
        self,
        scope: Construct,
        id: str,
        auto_delete_objects: bool = True,
        removal_policy: RemovalPolicy = RemovalPolicy.DESTROY,
        logging_prefix: Optional[str] = None,
        logging_bucket: Optional[s3.IBucket] = None,
        **kwargs,
    ):
        """Default bucket."""
        super().__init__(
            scope,
            id,
            encryption=s3.BucketEncryption.S3_MANAGED,  # S3 Managed encryption
            server_access_logs_bucket=logging_bucket,
            server_access_logs_prefix=logging_prefix,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,  # Public Access: BLOCK ALL # noqa: E501
            removal_policy=removal_policy,
            auto_delete_objects=auto_delete_objects,
            versioned=True,
            enforce_ssl=True,
            **kwargs,
        )
