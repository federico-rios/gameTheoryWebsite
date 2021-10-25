import numpy as np
from json import JSONEncoder
import json


class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


def np_to_bytes(array, name):
    np_data = {name: array}
    encoded_numpy_data = json.dumps(np_data, cls=NumpyArrayEncoder)  # use dump() to write
    bytes_numpy_data = bytes(encoded_numpy_data, encoding='utf8')
    return bytes_numpy_data


def bytes_to_np(json_bytes, name):
    json_string = json_bytes.decode('utf8')
    decoded_array = json.loads(json_string)
    np_array = np.asarray(decoded_array[name])
    return np_array



