import unittest
from main import get_1s

class TestGet1sFunction(unittest.TestCase):
    
    def test_with_10(self):
        """Test the function with 10."""
        result = get_1s(10)
        expected_result = [1] * 10
        self.assertEqual(result, expected_result)

    def test_with_default(self):
        """Test the function with default."""
        result = get_1s()
        expected_result = [1] * 30
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
