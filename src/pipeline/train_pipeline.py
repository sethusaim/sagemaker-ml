import sys

from src.entity.config_entity import PipelineConfig
from src.exception import CustomException
from src.entity.config_entity import DataIngestionConfig
from src.components.data_ingestion import DataIngestion


class TrainPipeline:
    is_pipeline_running: bool = False

    def __init__(self):
        self.pipeline_config = PipelineConfig()

    def start_data_ingestion(self):
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

    def run_pipeline(self):
        try:
            TrainPipeline.is_pipeline_running = True

            data_ingestion_artifact = self.start_data_ingestion()

        except Exception as e:
            raise CustomException(e, sys)
