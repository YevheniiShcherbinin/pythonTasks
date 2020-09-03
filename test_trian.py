# from trian import Triangle
# def test_area():
# assert Triangle(3, 4, 5) == int

# def test_perimeter():
# assert True

# def test_kind():
# assert True

import unittest

from unittest import TestCase
import trian


class TestTriangle(unittest.TestCase):

    def setUp(self):
        self.Triangle = trian.Triangle()

    def test_area(self):
        self.assertEqual(self.Triangle.area(4, 6, 7), 8)

    def test_perimeter(self):
        self.assertEqual(self.Triangle.perimeter(10, 12, 24), 46)

    def test_kind(self):
        self.assertEqual(self.Triangle.kind(8, 8, 10), "Isosceles")

    def test_exist(self):
        self.assertEqual(self.Triangle.kind(5, 3, 1), "Triangle not exist")

    def test_Versatile(self):
        self.assertEqual(self.Triangle.kind(12, 7, 4), "Versatile")

    def test_Rectangular(self):

        self.assertEqual(self.Triangle.kind(3, 4, 5), "Rectangular")

    def test_Equilateral(self):
        self.assertEqual(self.Triangle.kind(5, 5, 5), "Equilateral")

    if __name__ == "__main__":
        unittest.main()
