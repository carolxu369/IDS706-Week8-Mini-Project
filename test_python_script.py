import unittest
from python_script import process_data

class TestPythonScript(unittest.TestCase):

    def test_process_data(self):
        self.assertEqual(process_data(["1", "2", "3"]), ["2", "4", "6"])
        self.assertEqual(process_data(["0", "0", "0"]), ["0", "0", "0"])

if __name__ == "__main__":
    unittest.main()