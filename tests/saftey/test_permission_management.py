import unittest
import json
import os
from safety.permission_management import load_whitelist, load_user_permissions

class TestPermissionManagement(unittest.TestCase):
    
    def setUp(self):
        # Setting up mock whitelist and user_permissions files
        with open('whitelist.json', 'w') as f:
            json.dump({"TestFunc": True}, f)
        with open('user_permissions.json', 'w') as f:
            json.dump({"test_user": ["TestFunc"]}, f)
    
    def tearDown(self):
        # Clean up
        os.remove('whitelist.json')
        os.remove('user_permissions.json')
    
    def test_load_whitelist(self):
        whitelist = load_whitelist()
        self.assertIsInstance(whitelist, dict)
        self.assertEqual(whitelist.get("TestFunc"), True)
    
    def test_load_user_permissions(self):
        user_permissions = load_user_permissions()
        self.assertIsInstance(user_permissions, dict)
        self.assertEqual(user_permissions.get("test_user"), ["TestFunc"])

if __name__ == "__main__":
    unittest.main()
