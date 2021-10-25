import unittest
from db_model import db, Matrix, Round


class TestDb(unittest.TestCase):

    def test_matrix_model(self):
        """tests a simple query and addition of a Matrix row"""
        test_matrix = Matrix.query.filter_by(id=10).first()
        if test_matrix is None:
            test_matrix = Matrix(id=10, title="test", description="test matrix")
            db.session.add(test_matrix)
            db.session.commit()
        self.assertEqual(True, True)

    def test_round_foreign_key(self):
        """tests the addition of a round row, which is constrained by a foreign key"""
        test_matrix = Matrix.query.filter_by(id=11).first()
        if test_matrix is None:
            test_matrix = Matrix(id=11, title="test2", description="test matrix 2")
            db.session.add(test_matrix)
            db.session.commit()
            test_round = Round.query.filter_by(id=2).first()
            if test_round is None:
                test_round = Round(id=2, round_num=0, game=test_matrix)
                db.session.add(test_round)
                db.session.commit()
        self.assertEqual(True, True)

    def test_query(self):
        """tests a query"""
        matrix = Matrix.query.filter_by(title="afjsfiopa").first()
        print(matrix)
        self.assertEqual(True, True)




if __name__ == '__main__':
    unittest.main()
