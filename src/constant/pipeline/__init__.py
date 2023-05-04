from datetime import datetime
from time import gmtime, strftime

TIMESTAMP: datetime = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

ARTIFACTS_DIR: str = "artifacts"

PIPELINE_NAME: str = "sagemaker-demo"

## Data Ingestion Constants

DATA_INGESTION_DIR: str = "data_ingestion"

DATA_INGESTION_FILE_NAME: str = "mob_price_classification_train.csv"

FEATURE_STORE_BUCKET_NAME: str = "sagemaker-ineuron"

FEATURE_STORE_DATA_DIR: str = "data"

FEATURE_STORE_TRAIN_FILE_NAME: str = "mob_price_train.csv"

FEATURE_STORE_TEST_FILE_NAME: str = "mob_price_test.csv"

## Model Trainer Constants

FRAMEWORK_VERSION: str = "0.23-1"

SAGEMAKER_ESTIMATOR_ROLE: str = "arn:aws:iam::566373416292:role/service-role/AmazonSageMaker-ExecutionRole-20230120T164209"

INSTANCE_COUNT: int = 1

INSTANCE_TYPE: str = "ml.m5.large"

TRAIN_JOB_NAME: str = "RF-sklearn-sagemaker"

SPOT_INSTANCES: bool = True

MAX_WAIT: int = 7200

MAX_RUN: int = 3600

## Model Endpoint Constants

ENDPOINT_NAME: str = (
    f"RF-sklearn-sagemaker-endpoint-{strftime('%Y-%m-%d-%H-%M-%S', gmtime())}"
)

ENDPOINT_INSTANCE_COUNT: int = 1

ENDPOINT_INSTANCE_TYPE: str = "ml.m5.large"

## Model Predictor Config

PRED_BUCKET_NAME: str = "sagemaker-ineuron"

PRED_BUCKET_FILE_NAME: str = "mob_price_test.csv"

LOCAL_FILE_NAME: str = "mob_price_test.csv"
