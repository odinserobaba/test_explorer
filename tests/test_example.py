import unittest
import json

class TestExample(unittest.TestCase):
    def setUp(self):
        # Load parameters from JSON file
        with open('test_args.json') as f:
            self.params = json.load(f)

    def test_addition(self):
        param1 = self.params.get('param1', 'default_value1')
        param2 = self.params.get('param2', 'default_value2')
        self.assertEqual(1 + 1, 2)
        print(f"param1: {param1}, param2: {param2}")

    def test_subtraction(self):
        param1 = self.params.get('param1', 'default_value1')
        param2 = self.params.get('param2', 'default_value2')
        self.assertEqual(2 - 1, 1)
        print(f"param1: {param1}, param2: {param2}")
