import unittest

from elevators.elevators import elevator


class TestList(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(elevator(0, 1, 0), "left")
        self.assertEqual(elevator(0, 1, 1), "right")
        self.assertEqual(elevator(0, 1, 2), "right")
        self.assertEqual(elevator(0, 0, 0), "right")
        self.assertEqual(elevator(0, 2, 1), "right")


if __name__ == "__main__":
    unittest.main()
    print("Everything passed")
