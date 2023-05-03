import sys

from src.exception import CustomException
from src.pipeline.train_pipeline import TrainPipeline


def start_training():
    try:
        tp = TrainPipeline()

        tp.run_pipeline()

    except Exception as e:
        raise CustomException(e, sys)


if __name__ == "__main__":
    start_training()
