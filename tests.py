import unittest
import sys

# Tell unittest where to find boggle_solver.py and the Boggle class
sys.path.append("/home/codio/workspace/")

from boggle_solver import Boggle


class TestSuite_Alg_Scalability_Cases(unittest.TestCase):

    # ADD 4x4, 5x5, 6x6, 7x7...13x13, and LARGER Dictionaries
    def test_Normal_case_3x3(self):
        grid = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
        dictionary = ["abc", "abdhi", "abi", "ef", "cfi", "dea"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = sorted(x.upper() for x in solution)
        expected = sorted(x.upper() for x in ["abc", "abdhi", "cfi", "dea"])
        self.assertEqual(expected, solution)


class TestSuite_Simple_Edge_Cases(unittest.TestCase):
    # ADD MANY SIMPLE TEST CASES

    def test_SquareGrid_case_1x1(self):
        grid = [["A"]]
        dictionary = ["a", "b", "c"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = sorted(x.upper() for x in solution)
        expected = sorted([])  # no valid words in a 1x1 grid
        self.assertEqual(expected, solution)

    def test_EmptyGrid_case_0x0(self):
        grid = []  # truly empty grid
        dictionary = ["hello", "there", "general", "kenobi"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = sorted(x.upper() for x in solution)
        expected = sorted([])  # no words possible
        self.assertEqual(expected, solution)


class TestSuite_Complete_Coverage(unittest.TestCase):
    # ADD MANY COMPLEX TEST CASES
    def test_case_1(self):
        # Placeholder: add a real test later
        self.assertEqual(True, True)


class TestSuite_Qu_and_St(unittest.TestCase):
    # ADD QU AND ST TEST CASES
    def test_case_1(self):
        # Placeholder: add a real test later
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
