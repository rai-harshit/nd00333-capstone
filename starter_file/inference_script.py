import json
import numpy as np
import os
from sklearn.externals import joblib
from train import clean_data


def init():
    global model
    model_path = os.path.join(".","outputs","capstone-hyperdrive-model.joblib")
    model = joblib.load(model_path)

def run(data):
    try:
        data = np.array(json.loads(data))
        result = model.predict(data)
        return result.tolist()
    except Exception as e:
        error = str(e)
        return error