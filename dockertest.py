import unittest

class SimpleMath:
    @staticmethod
    def addition(x, y):
        return x + y

class TestSimpleMath(unittest.TestCase):
    def test_addition(self):
        result = SimpleMath.addition(1, 2)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()
