import sys

import boto3
from sagemaker.sklearn.estimator import SKLearn

from src.entity.artifact_entity import DataIngestionArtifact
from src.entity.config_entity import ModelTrainerConfig, ModelTunerConfig
from src.exception import CustomException


class ModelTrainer:
    def __init__(self, data_ingestion_artifact: DataIngestionArtifact):
        self.model_trainer_config = ModelTrainerConfig()

        self.tuner_config = ModelTunerConfig()

        self.data_ingestion_artifact = data_ingestion_artifact

        self.sagemaker_client = boto3.client("sagemaker")

    def train_and_save_model(self) -> str:
        try:
            sklearn_estimator = SKLearn(
                entry_point="src/ml/model/sagemaker_train_script.py",
                hyperparameters=self.tuner_config.hyperparameters,
                **self.model_trainer_config.estimator_config
            )

            sklearn_estimator.fit(
                {
                    "train": self.data_ingestion_artifact.feature_store_s3_train_file_path,
                    "test": self.data_ingestion_artifact.feature_store_s3_test_file_path,
                },
                wait=True,
            )

            sklearn_estimator.latest_training_job.wait(logs="None")

            model_artifact: str = self.sagemaker_client.describe_training_job(
                TrainingJobName=sklearn_estimator.latest_training_job.name
            )["ModelArtifacts"]["S3ModelArtifacts"]

            return model_artifact

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_model_training(self):
        try:
            model_artifact: str = self.train_and_save_model()

            return model_artifact

        except Exception as e:
            raise CustomException(e, sys)
