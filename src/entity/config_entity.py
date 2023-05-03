import os
from datetime import datetime

from src.constant import pipeline


class PipelineConfig:
    def __init__(self, timestamp=datetime.now()):
        timestamp: datetime = timestamp.strftime("%m_%d_%Y_%H_%M_%S")

        self.pipeline_name: str = pipeline.PIPELINE_NAME

        self.artifacts_dir: str = os.path.join(pipeline.ARTIFACTS_DIR, timestamp)


class DataIngestionConfig:
    def __init__(self, pipeline_config: PipelineConfig):
        self.data_ingestion_dir: str = os.path.join(
            pipeline_config.artifacts_dir, pipeline.DATA_INGESTION_DIR
        )

        self.data_ingestion_bucket_name: str = pipeline.FEATURE_STORE_BUCKET_NAME

        self.data_ingestion_file_name: str = pipeline.DATA_INGESTION_FILE_NAME

        self.feature_store_bucket_name: str = pipeline.FEATURE_STORE_BUCKET_NAME

        self.feature_store_data_dir: str = pipeline.FEATURE_STORE_DATA_DIR

        self.feature_store_train_file_name: str = pipeline.FEATURE_STORE_TRAIN_FILE_NAME

        self.feature_store_test_file_name: str = pipeline.FEATURE_STORE_TEST_FILE_NAME

        self.feature_store_file_path: str = os.path.join(
            self.data_ingestion_dir, self.data_ingestion_file_name
        )

        self.feature_store_train_file_path: str = os.path.join(
            self.data_ingestion_dir, self.feature_store_train_file_name
        )

        self.feature_store_test_file_path: str = os.path.join(
            self.data_ingestion_dir,
            self.feature_store_test_file_name,
        )
