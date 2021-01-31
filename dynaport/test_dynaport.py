import unittest
from dynaport import Dynaport


class TestDynaport(unittest.TestCase):
    def test_instantiation(self):
        dp = Dynaport()
        self.assertNotEqual(dp, "")


if __name__ == "__main__":
    unittest.main()
