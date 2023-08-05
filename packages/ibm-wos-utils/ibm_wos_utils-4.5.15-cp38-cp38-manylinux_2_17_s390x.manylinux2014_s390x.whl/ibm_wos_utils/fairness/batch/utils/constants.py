# ----------------------------------------------------------------------------------------------------
# IBM Confidential
# OCO Source Materials
# 5900-A3Q, 5737-H76
# Copyright IBM Corp. 2021
# The source code for this program is not published or other-wise divested of its trade 
# secrets, irrespective of what has been deposited with the U.S.Copyright Office.
# ----------------------------------------------------------------------------------------------------

"""
Contains constants used in the fairness spark jobs.
"""

BINARY_MODEL_TYPE = "binary"
MULTICLASS_MODEL_TYPE = "multiclass"
REGRESSION_MODEL_TYPE = "regression"

CATEGORICAL_DATA_TYPES = [
    "string"
]

NUMERICAL_DATA_TYPES = [
    "integer",
    "float",
    "double",
    "long"
]

SUPPORTED_STORAGE_TYPES = [
    "hive",
    "jdbc"
]

GROUP_BIAS_CALCULATION_WINDOW = 7  # In days

# Modelling roles
PREDICTION_MODELING_ROLE = "prediction"
PROBABILITY_MODELING_ROLE = "probability"
RECORD_ID_MODELING_ROLE = "record-id"
TIMESTAMP_MODELING_ROLE = "record-timestamp"
