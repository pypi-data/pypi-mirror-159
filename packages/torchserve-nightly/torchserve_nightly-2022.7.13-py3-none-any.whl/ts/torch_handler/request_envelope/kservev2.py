"""
The KServe Envelope is used to handle the KServe
Input Request inside Torchserve.
"""
import json
import logging
import numpy as np
from .base import BaseEnvelope

logger = logging.getLogger(__name__)

_DatatypeToNumpy = {
    "BOOL": "bool",
    "UINT8": "uint8",
    "UINT16": "uint16",
    "UINT32": "uint32",
    "UINT64": "uint64",
    "INT8": "int8",
    "INT16": "int16",
    "INT32": "int32",
    "INT64": "int64",
    "FP16": "float16",
    "FP32": "float32",
    "FP64": "float64",
    "BYTES": "byte",
}

_NumpyToDatatype = {value: key for key, value in _DatatypeToNumpy.items()}

# NOTE: numpy has more types than v2 protocol
_NumpyToDatatype["object"] = "BYTES"

# Adding support for unicode string
# Ref: https://numpy.org/doc/stable/reference/arrays.dtypes.html
_NumpyToDatatype["U"] = "BYTES"


def _to_dtype(datatype: str) -> "np.dtype":
    dtype = _DatatypeToNumpy[datatype]
    return np.dtype(dtype)


def _to_datatype(dtype: np.dtype) -> str:
    as_str = str(dtype)
    if as_str not in _NumpyToDatatype:
        as_str = getattr(dtype, "kind")
    datatype = _NumpyToDatatype[as_str]

    return datatype


class KServev2Envelope(BaseEnvelope):
    """Implementation. Captures batches in KServe v2 protocol format, returns
    also in FServing v2 protocol format.
    """

    def parse_input(self, data):
        """Translates KServe request input to list of data expected by Torchserve.

        Parameters:
        data (json): KServe v2 request input json.
        {
          "inputs": [{
            "name": "input-0",
            "shape": [37],
            "datatype": "INT64",
            "data": [66, 108, 111, 111, 109]
          }]
        }

        Returns: list of data objects.
        [{
        'name': 'input-0',
        'shape': [5],
        'datatype': 'INT64',
        'data': [66, 108, 111, 111, 109]
        }]

        """
        logger.debug("Parsing input in KServe v2 format %s", data)
        inputs = self._batch_from_json(data)
        logger.debug("KServev2 parsed inputs %s", inputs)
        return inputs

    def _batch_from_json(self, rows):
        """
        Joins the instances of a batch of JSON objects
        """
        logger.debug("Parse input data %s", rows)
        body_list = [body_list.get("data") or body_list.get("body") for body_list in rows]
        data_list = self._from_json(body_list)
        return data_list

    def _from_json(self, body_list):
        """
        Extracts the data from the JSON object
        """
        # If the KF Transformer and Explainer sends in data as bytesarray
        if isinstance(body_list[0], (bytes, bytearray)):
            body_list = [json.loads(body.decode()) for body in body_list]
            logger.debug("Bytes array is %s", body_list)
        if "id" in body_list[0]:
            setattr(self.context, "input_request_id", body_list[0]["id"])
        data_list = [inputs_list.get("inputs") for inputs_list in body_list][0]
        return data_list

    def format_output(self, data):
        """Translates Torchserve output KServe v2 response format.

        Parameters:
        data (list): Torchserve response for handler.

        Returns: KServe v2 response json.
        {
          "id": "f0222600-353f-47df-8d9d-c96d96fa894e",
          "model_name": "bert",
          "model_version": "1",
          "outputs": [{
            "name": "predict",
            "shape": [1],
            "datatype": "INT64",
            "data": [2]
          }]
        }

        """
        logger.debug("The Response of KServe v2 format %s", data)
        response = {}
        if hasattr(self.context, "input_request_id"):
            response["id"] = getattr(self.context, "input_request_id")
            delattr(self.context, "input_request_id")
        else:
            response["id"] = self.context.get_request_id(0)
        response["model_name"] = self.context.manifest.get("model").get(
            "modelName")
        response["model_version"] = self.context.manifest.get("model").get(
            "modelVersion")
        response["outputs"] = self._batch_to_json(data)
        return [response]

    def _batch_to_json(self, data):
        """
        Splits batch output to json objects
        """
        output = []
        for item in data:
            output.append(self._to_json(item))
        return output

    def _to_json(self, data):
        """
        Constructs JSON object from data
        """
        output_data = {}
        data_ndarray = np.array(data)
        output_data["name"] = ("explain" if self.context.get_request_header(
            0, "explain") == "True" else "predict")
        output_data["shape"] = list(data_ndarray.shape)
        output_data["datatype"] = _to_datatype(data_ndarray.dtype)
        output_data["data"] = data_ndarray.flatten().tolist()
        return output_data
