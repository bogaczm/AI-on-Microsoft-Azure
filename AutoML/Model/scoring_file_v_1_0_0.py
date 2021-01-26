# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
import json
import logging
import os
import pickle
import numpy as np
import pandas as pd
import joblib

import azureml.automl.core
from azureml.automl.core.shared import logging_utilities, log_server
from azureml.telemetry import INSTRUMENTATION_KEY

from inference_schema.schema_decorators import input_schema, output_schema
from inference_schema.parameter_types.numpy_parameter_type import NumpyParameterType
from inference_schema.parameter_types.pandas_parameter_type import PandasParameterType


input_sample = pd.DataFrame({"bedrooms": pd.Series([0.0], dtype="float64"), "bathrooms": pd.Series([0.0], dtype="float64"), "sqft_living": pd.Series([0.0], dtype="float64"), "sqft_lot": pd.Series([0], dtype="int64"), "floors": pd.Series([0.0], dtype="float64"), "waterfront": pd.Series([0], dtype="int64"), "view": pd.Series([0], dtype="int64"), "condition": pd.Series([0], dtype="int64"), "grade": pd.Series([0], dtype="int64"), "sqft_above": pd.Series([0], dtype="int64"), "sqft_basement": pd.Series([0], dtype="int64"), "yr_built": pd.Series([0], dtype="int64"), "yr_renovated": pd.Series([0], dtype="int64"), "lat": pd.Series([0.0], dtype="float64"), "long": pd.Series([0.0], dtype="float64"), "sqft_living15": pd.Series([0.0], dtype="float64"), "sqft_lot15": pd.Series([0.0], dtype="float64"), "month": pd.Series([0], dtype="int64"), "year": pd.Series([0], dtype="int64"), "bedrooms_squared": pd.Series([0.0], dtype="float64"), "bed_bath_rooms": pd.Series([0.0], dtype="float64"), "log_sqft_living": pd.Series([0.0], dtype="float64"), "sqft_rooms": pd.Series([0.0], dtype="float64"), "condition_advanced": pd.Series([0], dtype="int64")})
output_sample = np.array([0])
try:
    log_server.enable_telemetry(INSTRUMENTATION_KEY)
    log_server.set_verbosity('INFO')
    logger = logging.getLogger('azureml.automl.core.scoring_script')
except:
    pass


def init():
    global model
    # This name is model.id of model that we want to deploy deserialize the model file back
    # into a sklearn model
    model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'model.pkl')
    path = os.path.normpath(model_path)
    path_split = path.split(os.sep)
    log_server.update_custom_dimensions({'model_name': path_split[1], 'model_version': path_split[2]})
    try:
        logger.info("Loading model from path.")
        model = joblib.load(model_path)
        logger.info("Loading successful.")
    except Exception as e:
        logging_utilities.log_traceback(e, logger)
        raise


@input_schema('data', PandasParameterType(input_sample))
@output_schema(NumpyParameterType(output_sample))
def run(data):
    try:
        result = model.predict(data)
        return json.dumps({"result": result.tolist()})
    except Exception as e:
        result = str(e)
        return json.dumps({"error": result})
