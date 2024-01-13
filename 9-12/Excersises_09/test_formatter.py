"""
SAMPLE CODE BY POIN
"""

import unittest
import formatter

class TestFormatter(unittest.TestCase):
def test_upper(self):
    test_text = "John ORaw"
    result = formatter.convert_upper(test_text)
    self.assertEqual(result, "JoHN ORAW")

    def test_upper(self):
        test_text = "John ORaw"
        result = formatter.convert_upper(test_text)
        self.assertEqual(result, "JOHN ORAW")

if __name__ =="__main__":
    unittest.main()
