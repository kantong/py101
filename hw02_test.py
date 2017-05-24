import unittest
import hw02


class TestHw02(unittest.TestCase):

    def testProduct(self):
        self.assertEqual(hw02.product(0, hw02.identity), 0)
        self.assertEqual(hw02.product(1, hw02.identity), 1)
        self.assertEqual(hw02.product(3, hw02.identity), 6)
        self.assertEqual(hw02.product(5, hw02.identity), 120)
        self.assertEqual(hw02.product(5, hw02.identity), 120)
        with self.assertRaises(AssertionError):
            hw02.product(-1, hw02.identity)


if __name__ == '__main__':
    unittest.main()