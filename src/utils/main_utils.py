import sys

from src.exception import CustomException


def save_object():
    try:
        pass

    except Exception as e:
        raise CustomException(e, sys)


# model_path = os.path.join(args.model_dir, "model.joblib")

# joblib.dump(model, model_path)
