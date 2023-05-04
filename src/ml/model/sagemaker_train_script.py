import argparse
import os

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


def model_fn(model_dir):
    clf = joblib.load(os.path.join(model_dir, "model.joblib"))

    return clf


if __name__ == "__main__":
    print("[INFO] Extracting arguments")

    parser = argparse.ArgumentParser()

    # hyperparameters sent by the client are passed as command-line arguments to the script.
    parser.add_argument("--n_estimators", type=int, default=100)

    parser.add_argument("--random_state", type=int, default=0)

    # Data, model, and output directories
    parser.add_argument("--model-dir", type=str, default=os.environ.get("SM_MODEL_DIR"))

    parser.add_argument("--train", type=str, default=os.environ.get("SM_CHANNEL_TRAIN"))

    parser.add_argument("--test", type=str, default=os.environ.get("SM_CHANNEL_TEST"))

    parser.add_argument("--train_file", type=str, default="mob_price_train.csv")

    parser.add_argument("--test_file", type=str, default="mob_price_test.csv")

    args, _ = parser.parse_known_args()

    print("[INFO] Reading data")

    train_df = pd.read_csv(os.path.join(args.train, args.train_file))

    test_df = pd.read_csv(os.path.join(args.test, args.test_file))

    features = list(train_df.columns)

    label = features.pop(-1)

    print("Building training and testing datasets")

    X_train = train_df[features]

    X_test = test_df[features]

    y_train = train_df[label]

    y_test = test_df[label]

    print("Column order: ")

    print(features)

    print("Label column is: ", label)

    print("Data Shape: ")

    print("---- SHAPE OF TRAINING DATA (85%) ----")

    print(X_train.shape)

    print(y_train.shape)

    print("---- SHAPE OF TESTING DATA (15%) ----")

    print(X_test.shape)

    print(y_test.shape)

    print("Training RandomForest Model.....")

    model = RandomForestClassifier(
        n_estimators=args.n_estimators,
        random_state=args.random_state,
        verbose=3,
        n_jobs=-1,
    )
    model.fit(X_train, y_train)

    model_path = os.path.join(args.model_dir, "model.joblib")

    joblib.dump(model, model_path)

    print("Model persisted at " + model_path)

    y_pred_test = model.predict(X_test)

    test_acc = accuracy_score(y_test, y_pred_test)

    test_rep = classification_report(y_test, y_pred_test)

    print("---- METRICS RESULTS FOR TESTING DATA ----")

    print("Total Rows are: ", X_test.shape[0])

    print("[TESTING] Model Accuracy is: ", test_acc)

    print("[TESTING] Testing Report: ")

    print(test_rep)
