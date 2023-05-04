import sys

from src.components.data_ingestion import DataIngestion
from src.components.model_trainer import ModelTrainer
from src.entity.artifact_entity import DataIngestionArtifact
from src.entity.config_entity import DataIngestionConfig, PipelineConfig
from src.exception import CustomException


class TrainPipeline:
    is_pipeline_running: bool = False

    def __init__(self):
        self.pipeline_config = PipelineConfig()

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            self.data_ingestion_config = DataIngestionConfig(
                pipeline_config=self.pipeline_config
            )

            data_ingestion = DataIngestion(
                data_ingestion_config=self.data_ingestion_config
            )

            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

            return data_ingestion_artifact

        except Exception as e:
            raise CustomException(e, sys)

    def start_model_training(
        self, data_ingestion_artifact: DataIngestionArtifact
    ) -> str:
        try:
            model_trainer = ModelTrainer(
                data_ingestion_artifact=data_ingestion_artifact
            )

            model_trainer_artifact: str = model_trainer.initiate_model_training()

            return model_trainer_artifact

        except Exception as e:
            raise CustomException(e, sys)

    def run_pipeline(self):
        try:
            TrainPipeline.is_pipeline_running = True

            data_ingestion_artifact: DataIngestionArtifact = self.start_data_ingestion()

            model_trainer_artifact: str = self.start_model_training(
                data_ingestion_artifact=data_ingestion_artifact
            )

        except Exception as e:
            raise CustomException(e, sys)