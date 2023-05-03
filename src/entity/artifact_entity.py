from dataclasses import dataclass


@dataclass
class DataIngestionArtifact:
    feature_store_s3_train_file_path: str

    feature_store_s3_test_file_path: str
