from datetime import datetime
from typing import Dict

from src.constant import pipeline


class PipelineConfig:
    def __init__(self, timestamp=datetime.now()):
        timestamp: datetime = timestamp.strftime("%m_%d_%Y_%H_%M_%S")

        self.pipeline_name: str = pipeline.PIPELINE_NAME

        self.artifacts_dir: str = pipeline.ARTIFACTS_DIR + "/" + timestamp


class DataIngestionConfig:
    def __init__(self, pipeline_config: PipelineConfig):
        self.data_ingestion_dir: str = (
            pipeline_config.artifacts_dir + "/" + pipeline.DATA_INGESTION_DIR
        )

        self.feature_store_bucket_name: str = pipeline.FEATURE_STORE_BUCKET_NAME

        self.feature_store_data_dir: str = pipeline.FEATURE_STORE_DATA_DIR

        self.feature_store_file_path: str = (
            self.data_ingestion_dir + "/" + pipeline.DATA_INGESTION_FILE_NAME
        )

        self.feature_store_train_file_path: str = (
            self.data_ingestion_dir + "/" + pipeline.FEATURE_STORE_TRAIN_FILE_NAME
        )

        self.feature_store_test_file_path: str = (
            self.data_ingestion_dir + "/" + pipeline.FEATURE_STORE_TEST_FILE_NAME
        )


class ModelTunerConfig:
    def __init__(self):
        self.hyperparameters: Dict = {"n_estimators": 100, "random_state": 0}


class ModelTrainerConfig:
    def __init__(self):
        self.estimator_config: Dict = {
            "instance_count": pipeline.INSTANCE_COUNT,
            "instance_type": pipeline.INSTANCE_TYPE,
            "framework_verion": pipeline.FRAMEWORK_VERSION,
            "base_job_name": pipeline.TRAIN_JOB_NAME,
            "use_spot_instances": pipeline.SPOT_INSTANCES,
            "max_wait": 7200,
            "max_run": 3600,
            "framework_version": pipeline.FRAMEWORK_VERSION,
            "role": pipeline.SAGEMAKER_ESTIMATOR_ROLE,
        }


class EndPointConfig:
    def __init__(self):
        self.model_endpoint_config: Dict = {
            "name": pipeline.ENDPOINT_NAME,
            "role": pipeline.SAGEMAKER_ESTIMATOR_ROLE,
            "framework_version": pipeline.FRAMEWORK_VERSION,
        }

        self.model_deploy_config: Dict = {
            "endpoint_name": pipeline.ENDPOINT_NAME,
            "initial_instance_count": pipeline.ENDPOINT_INSTANCE_COUNT,
            "instance_type": pipeline.ENDPOINT_INSTANCE_TYPE,
        }


class PredictorConfig:
    def __init__(self):
        self.pred_bucket_name: str = pipeline.PRED_BUCKET_NAME

        self.pred_bucket_file_name: str = pipeline.PRED_BUCKET_FILE_NAME

        self.pred_local_file_name: str = pipeline.LOCAL_FILE_NAME
