import os
import sys

from src.exception import CustomException
from src.logger import logging
import boto3


class AWSOperation:
    def __init__(self):
        self.s3_client = boto3.client("s3")

    def sync_folder_to_s3(
        self, folder: str, bucket_name: str, bucket_folder_name: str
    ) -> None:
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
        try:
            self.s3_client.download_file(bucket_name, bucket_file_name, local_file_name)

            return local_file_name

        except Exception as e:
            raise CustomException(e, sys)
