import numpy as np
from json import JSONEncoder
import json


class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


def np_to_json(array, name):
    np_data = {name: array}
    encoded_numpy_data = json.dumps(np_data, cls=NumpyArrayEncoder)  # use dump() to write
    return encoded_numpy_data


def json_to_np(json_string, name):
    decoded_array = json.loads(json_string)
    return np.asarray(decoded_array[name])



