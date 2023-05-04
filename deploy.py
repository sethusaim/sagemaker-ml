import sys

from sagemaker.sklearn.estimator import SKLearnModel

from src.entity.config_entity import EndPointConfig
from src.exception import CustomException


class DeployModel:
    def __init__(self):
        self.model_endpoint_config = EndPointConfig()

    def deploy_model(self, model_artifact_path: str) -> None:
        try:
            model = SKLearnModel(
                model_data=model_artifact_path,
                entry_point="src/ml/model/sagemaker_train_script.py",
                **self.model_endpoint_config.model_endpoint_config
            )

            model.deploy(**self.model_endpoint_config.model_deploy_config)

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    deploy = DeployModel()

    deploy.deploy_model(
        model_artifact_path="s3://sagemaker-us-east-1-566373416292/RF-sklearn-sagemaker-2023-05-04-09-05-19-827/output/model.tar.gz"
    )
