import os
import sys

import boto3

from src.exception import CustomException
from src.logger import logging


class AWSOperation:
    def __init__(self):
        self.s3_client = boto3.client("s3")

    def sync_folder_to_s3(
        self, folder: str, bucket_name: str, bucket_folder_name: str
    ) -> None:
        """
        This function syncs a local folder to an S3 bucket using the AWS CLI.

        Args:
          folder (str): The local folder path that needs to be synced to S3 bucket.
          bucket_name (str): The name of the S3 bucket where the folder will be synced to.
          bucket_folder_name (str): The name of the folder in the S3 bucket where the contents of the local
        folder will be synced to.
        """
        logging.info("Entered sync_folder_to_s3 method of AWSOperation class")

        try:
            command: str = (
                f"aws s3 sync {folder} s3://{bucket_name}/{bucket_folder_name}/ "
            )

            os.system(command)

            logging.info(f"Executed {command} command")

            logging.info("Exited sync_folder_to_s3 method of AWSOperation class")

        except Exception as e:
            raise CustomException(e, sys)

    def sync_folder_from_s3(
        self, folder: str, bucket_name: str, bucket_folder_name: str
    ) -> None:
        """
        The function syncs a local folder with a specified folder in an S3 bucket using the AWS CLI.

        Args:
          folder (str): The local folder path where the files from S3 bucket will be synced to.
          bucket_name (str): The name of the S3 bucket from which the folder needs to be synced.
          bucket_folder_name (str): The name of the folder within the S3 bucket that needs to be synced with
        the local folder.
        """
        logging.info("Entered sync_folder_from_s3 method of AWSOperation class")
        try:
            command: str = (
                f"aws s3 sync s3://{bucket_name}/{bucket_folder_name}/ {folder} "
            )

            os.system(command)

            logging.info(f"Executed the {command} command")

            logging.info("Exited sync_folder_from_s3 method of AWSOperation class")

        except Exception as e:
            raise CustomException(e, sys)

    def download_file(
        self, bucket_name: str, bucket_file_name: str, local_file_name: str
    ) -> str:
        """
        The function downloads a file from an AWS S3 bucket and saves it locally.

        Args:
          bucket_name (str): The name of the S3 bucket from which the file needs to be downloaded.
          bucket_file_name (str): The name of the file in the S3 bucket that needs to be downloaded.
          local_file_name (str): The name of the file that will be created on the local machine after
        downloading from the S3 bucket.

        Returns:
          The method is returning the name of the local file that was downloaded from the specified S3
        bucket.
        """
        logging.info("Entered download_file method of AWSOperation class")

        try:
            logging.info(f"Downloading {bucket_file_name} file from {bucket_name}")

            self.s3_client.download_file(bucket_name, bucket_file_name, local_file_name)

            logging.info(
                f"Downloaded {bucket_file_name} file from {bucket_name} bucket to {local_file_name} file "
            )

            logging.info("Exited download_file method of AWSOperation class")

            return local_file_name

        except Exception as e:
            raise CustomException(e, sys)
