import sys

import boto3
from sagemaker.sklearn.estimator import SKLearn

from src.entity.artifact_entity import DataIngestionArtifact
from src.entity.config_entity import ModelTrainerConfig, ModelTunerConfig
from src.exception import CustomException
from src.logger import logging


class ModelTrainer:
    def __init__(self, data_ingestion_artifact: DataIngestionArtifact):
        self.model_trainer_config = ModelTrainerConfig()

        self.tuner_config = ModelTunerConfig()

        self.data_ingestion_artifact = data_ingestion_artifact

        self.sagemaker_client = boto3.client("sagemaker")

    def initiate_model_training(self) -> str:
        """
        This function initiates model training using an SKLearn estimator and returns the S3 path of the
        trained model artifact.

        Returns:
          The method `initiate_model_training` returns a string which is the S3 path of the trained model
        artifact.
        """
        logging.info("Entered initiate_model_training method of ModelTrainer class")

        try:
            sklearn_estimator = SKLearn(
                entry_point="src/ml/model/sagemaker_train_script.py",
                hyperparameters=self.tuner_config.hyperparameters,
                **self.model_trainer_config.estimator_config,
            )

            logging.info(
                f"Created sklearn estimator with {self.tuner_config.hyperparameters} hyperparameters"
            )

            sklearn_estimator.fit(
                {
                    "train": self.data_ingestion_artifact.feature_store_s3_train_file_path,
                    "test": self.data_ingestion_artifact.feature_store_s3_test_file_path,
                },
                wait=True,
            )

            logging.info(
                f"Training the estimator with {self.data_ingestion_artifact.feature_store_s3_train_file_path} and {self.data_ingestion_artifact.feature_store_s3_test_file_path} train and test file path"
            )

            sklearn_estimator.latest_training_job.wait(logs="None")

            model_artifact: str = self.sagemaker_client.describe_training_job(
                TrainingJobName=sklearn_estimator.latest_training_job.name
            )["ModelArtifacts"]["S3ModelArtifacts"]

            logging.info(f"Got {model_artifact} model path from latest training job")

            logging.info("Exited initiate_model_training method of ModelTrainer class")

            return model_artifact

        except Exception as e:
            raise CustomException(e, sys)
