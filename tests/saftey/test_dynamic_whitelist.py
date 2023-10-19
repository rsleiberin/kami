# test_dynamic_whitelist.py
import unittest
from safety.dynamic_whitelist import DynamicWhitelist

class TestDynamicWhitelist(unittest.TestCase):

    def setUp(self):
        self.dw = DynamicWhitelist()

    def test_add_to_whitelist(self):
        self.dw.add_to_whitelist("TestClass", "test_module")
        self.assertTrue(self.dw.is_whitelisted("TestClass"))

    def test_remove_from_whitelist(self):
        self.dw.add_to_whitelist("TestClass", "test_module")
        self.dw.remove_from_whitelist("TestClass")
        self.assertFalse(self.dw.is_whitelisted("TestClass"))

    def test_is_whitelisted(self):
        self.dw.add_to_whitelist("TestClass", "test_module")
        self.assertTrue(self.dw.is_whitelisted("TestClass"))
        self.assertFalse(self.dw.is_whitelisted("NonExistentClass"))

    def test_persistence(self):
        self.dw.add_to_whitelist("PersistentClass", "test_module")
        new_dw = DynamicWhitelist()
        self.assertTrue(new_dw.is_whitelisted("PersistentClass"))

    def test_edge_cases(self):
        self.dw.add_to_whitelist("TestClass", "test_module")
        self.dw.add_to_whitelist("TestClass", "test_module")
        self.assertTrue(self.dw.is_whitelisted("TestClass"))

        with self.assertRaises(KeyError):
            self.dw.remove_from_whitelist("NonExistentClass")

if __name__ == "__main__":
    unittest.main()
