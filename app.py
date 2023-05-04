from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from sagemaker.sklearn.estimator import SKLearnModel
from starlette.responses import RedirectResponse
from uvicorn import run as app_run

from src.constant.pipeline import APP_HOST, APP_PORT
from src.entity.config_entity import EndPointConfig
from src.ml.model.estimator import CustomEstimator
from src.pipeline.train_pipeline import TrainPipeline

app = FastAPI()

endpoint_config = EndPointConfig()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")


@app.get("/train")
async def training():
    try:
        tp = TrainPipeline()

        tp.run_pipeline()

        return Response("Training successful !!")

    except Exception as e:
        return Response(f"Error Occurred! {e}")


@app.post("/deploy/{s3_model_uri:path}")
async def deploy_model(s3_model_uri: str):
    try:
        model = SKLearnModel(
            model_data=s3_model_uri,
            entry_point="src/ml/model/sagemaker_train_script.py",
            **endpoint_config.model_endpoint_config,
        )

        model.deploy(**endpoint_config.model_deploy_config)

        return Response(f"{s3_model_uri} model deployment successfully")

    except Exception as e:
        return Response(f"Error Occurred! {e}")


@app.post("/predict/{endpoint_name}")
async def predict(endpoint_name: str):
    try:
        estimator = CustomEstimator()

        predictions = estimator.predict(endpoint_name=endpoint_name)

        return Response(f"Model Predictions are {predictions}")

    except Exception as e:
        return Response(f"Error Occurred! {e}")


if __name__ == "__main__":
    app_run(app, host=APP_HOST, port=APP_PORT)
