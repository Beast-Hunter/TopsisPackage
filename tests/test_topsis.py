import unittest
import numpy as np
from topsis.__main__ import topsis

class TestTopsis(unittest.TestCase):

    def setUp(self):

        self.data = np.array([
            [10, 20, 30],
            [20, 30, 40],
            [30, 10, 20]
        ])

        self.weights = [0.3, 0.5, 0.2]

        self.impacts = ['+', '+', '-']

    def testCorrectness(self):
        expectedScore = [0.4231, 0.6723, 0.7987]
        expectedRank = [3, 2, 1]

        score, rank = topsis(self.data, self.weights, self.impacts)

        np.testing.assert_almost_equal(score, expectedScore, decimal = 4)
        np.testing.assert_almost_equal(rank, expectedRank)

    def testInvalidWeightLength(self):
        invalidWeights = [0.3, 0.5]

        with self.assertRaises(ValueError):
            topsis(self.data, invalidWeights, self.impacts)

    def testInvalidWeightLength(self):
        invalidImpacts = ['+', '+']

        with self.assertRaises(ValueError):
            topsis(self.data, self.weights, invalidImpacts)

    def testNonNumericData(self):
        invalidData = np.array([
            [10, 'A', 30],
            [20, 30, 40],
        ])

        with self.assertRaises(ValueError):
            topsis(invalidData, self.weights, self.impacts)

    def testSingleAlternative(self):
        singleData = np.array([[10, 20, 30]])
        score, rank = topsis(singleData, self.weights, self.impacts)
        self.assertEqual(score.shape[0], 1)
        self.assertEqual(rank[0], 1)

    def testAllSameValues(self):
        sameData = np.array([
            [10, 10, 10],
            [10, 10, 10],
        ])
        score, rank = topsis(sameData, self.weights, self.impacts)
        self.assertTrue(np.allclose(score, 0.5))
        self.assertTrue(np.array_equal(rank, [1, 1]))
