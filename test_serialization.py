import unittest
import numpy as np
from numpy_to_db import np_to_bytes, bytes_to_np


class TestSerialization(unittest.TestCase):
    def test_encoding_and_decoding(self):
        original_array = np.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])
        name = "array"
        encoded_array = np_to_bytes(original_array, name)
        #print(encoded_array)

        restored_array = bytes_to_np(encoded_array, name)
        print(original_array)
        print(restored_array)
        self.assertEqual(original_array.all(), restored_array.all())  # add assertion here


if __name__ == '__main__':
    unittest.main()
