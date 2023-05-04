import sys

import pandas as pd
from sagemaker import Session
from sagemaker.predictor import Predictor
from sagemaker.serializers import CSVSerializer

from src.cloud_storage.aws_operations import AWSOperation
from src.entity.config_entity import PredictorConfig
from src.exception import CustomException


class CustomEstimator:
    def __init__(self):
        self.sagemaker_session = Session()

        self.aws_op = AWSOperation()

        self.predictor_config = PredictorConfig()

    def predict(self, endpoint_name: str) -> str:
        try:
            file_name = self.aws_op.download_file(
                bucket_name=self.predictor_config.pred_bucket_name,
                bucket_file_name=self.predictor_config.pred_bucket_file_name,
                local_file_name=self.predictor_config.pred_local_file_name,
            )

            df = pd.read_csv(file_name)

            features = list(df.columns)

            features.pop(-1)

            input_payload = df[features][0:2].values.tolist()

            predictor = Predictor(
                endpoint_name=endpoint_name,
                sagemaker_session=self.sagemaker_session,
                serializer=CSVSerializer(),
            )

            res = predictor.predict(input_payload).decode("utf-8")

            return res

        except Exception as e:
            raise CustomException(e, sys)
