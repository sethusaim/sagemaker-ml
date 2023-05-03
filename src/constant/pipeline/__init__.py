from datetime import datetime

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
