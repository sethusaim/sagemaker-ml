import sys

import pandas as pd
from sklearn.model_selection import train_test_split

from src.cloud_storage.aws_operations import AWSOperation
from src.entity.artifact_entity import DataIngestionArtifact
from src.entity.config_entity import DataIngestionConfig
from src.exception import CustomException
from src.logger import logging


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        self.aws_op = AWSOperation()

        self.data_ingestion_config = data_ingestion_config

    def get_data_from_s3(self) -> pd.DataFrame:
        """
        This function retrieves data from an S3 bucket and returns it as a Pandas DataFrame.

        Returns:
          a pandas DataFrame object.
        """
        logging.info(
            "Entered export_data_to_feature_store method of DataIngestion class"
        )

        try:
            self.aws_op.sync_folder_from_s3(
                folder=self.data_ingestion_config.data_ingestion_dir,
                bucket_name=self.data_ingestion_config.feature_store_bucket_name,
                bucket_folder_name=self.data_ingestion_config.feature_store_data_dir,
            )

            data_df: pd.DataFrame = pd.read_csv(
                self.data_ingestion_config.feature_store_file_path
            )

            logging.info(
                f"Read dataframe from {self.data_ingestion_config.feature_store_file_path} file"
            )

            logging.info(
                "Exited export_data_to_feature_store method of DataIngestion class"
            )

            return data_df

        except Exception as e:
            raise CustomException(e, sys)

    def split_data(self, dataframe: pd.DataFrame) -> None:
        """
        The function splits a given dataframe into train and test sets, saves them as CSV files, and logs
        the process.

        Args:
          dataframe (pd.DataFrame): A pandas DataFrame containing the data to be split into train and test
        sets.
        """
        logging.info("Entered split_data method of DataIngestion class")

        try:
            logging.info(
                f"Read the dataframe from {self.data_ingestion_config.feature_store_file_path}"
            )

            train_set, test_set = train_test_split(
                dataframe, test_size=0.2, random_state=42
            )

            logging.info(f"Performed train test split on the dataset")

            train_set.to_csv(
                self.data_ingestion_config.feature_store_train_file_path,
                index=False,
                header=True,
            )

            test_set.to_csv(
                self.data_ingestion_config.feature_store_test_file_path,
                index=False,
                header=True,
            )

            logging.info(
                f"Converted train set and test set to {self.data_ingestion_config.feature_store_train_file_path} file and {self.data_ingestion_config.feature_store_test_file_path} file"
            )

            logging.info("Exited split_data method of DataIngestion class")

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        """
        This function initiates data ingestion by getting data from S3, splitting it, syncing it to S3, and
        returning a DataIngestionArtifact.
        
        Returns:
          The method `initiate_data_ingestion` returns an instance of the `DataIngestionArtifact` class.
        """
        logging.info("Entered initiate_data_ingestion method of DataIngestion class")

        try:
            dataframe: pd.DataFrame = self.get_data_from_s3()

            self.split_data(dataframe=dataframe)

            self.aws_op.sync_folder_to_s3(
                folder=self.data_ingestion_config.data_ingestion_dir,
                bucket_name=self.data_ingestion_config.feature_store_bucket_name,
                bucket_folder_name=self.data_ingestion_config.data_ingestion_dir,
            )

            feature_store_s3_train_file_path: str = f"s3://{self.data_ingestion_config.feature_store_bucket_name}/{self.data_ingestion_config.feature_store_train_file_path}"

            feature_store_s3_test_file_path: str = f"s3://{self.data_ingestion_config.feature_store_bucket_name}/{self.data_ingestion_config.feature_store_test_file_path}"

            data_ingestion_artifact = DataIngestionArtifact(
                feature_store_s3_train_file_path=feature_store_s3_train_file_path,
                feature_store_s3_test_file_path=feature_store_s3_test_file_path,
            )

            logging.info("Exited initiate_data_ingestion method of DataIngestion class")

            return data_ingestion_artifact

        except Exception as e:
            raise CustomException(e, sys)
