# from trian import Triangle
# def test_area():
# assert Triangle(3, 4, 5) == int

# def test_perimeter():
# assert True

# def test_kind():
# assert True
import unittest
from trian import Triangle


class TestTriangle(unittest.TestCase):

    def setUp(self):
        self.Triangle = Triangle()

    def area(self):
        self.assertEqual(self.Triangle.area(4, 6, 7), 8)

        if __name__ == "__main__":
            unittest.main()
