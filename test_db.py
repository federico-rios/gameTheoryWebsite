import unittest
from db_model import db, Matrix, Round
import numpy as np
from numpy_to_db import np_to_bytes, bytes_to_np

class TestDb(unittest.TestCase):

    def test_matrix_model(self):
        """tests a simple query and addition of a Matrix row"""
        test_matrix = Matrix.query.filter_by(id=10).first()
        if test_matrix is None:
            a = np_to_bytes(np.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]]), "a")
            b = np_to_bytes(np.array([[77, 88, 99], [44, 55, 66], [11, 22, 33]]), "b")
            test_matrix = Matrix(
                id=10,
                title="test",
                description="test matrix",
                matrix_a=a,
                matrix_b=b
            )
            db.session.add(test_matrix)
            db.session.commit()
        test_matrix = Matrix.query.filter_by(id=10).first()
        print(test_matrix)
        self.assertTrue(test_matrix is not None)

    def test_round_foreign_key(self):
        """tests the addition of a round row, which is constrained by a foreign key"""

        """test_matrix = Matrix.query.filter_by(id=11).first()
        if test_matrix is None:
            test_matrix = Matrix(id=11, title="test2", description="test matrix 2")
            db.session.add(test_matrix)
            db.session.commit()

        test_round = Round.query.filter_by(id=2).first()
        if test_round is None:
            test_round = Round(id=2, round_num=0, game=test_matrix)
            db.session.add(test_round)
            db.session.commit()
        test_round = Round.query.filter_by(id=2).first()
        self.assertTrue(test_round is not None)"""

    def test_query(self):
        """tests a query"""
        """matrix = Matrix.query.filter_by(title="afjsfiopa").first()
        print(matrix)
        self.assertTrue(matrix is None)"""

if __name__ == '__main__':
    unittest.main()
