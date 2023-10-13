import unittest
from unittest.mock import patch
from modules.databases.airtable_client.airtable_client import AirtableClient
from modules.utils.error_handler import handle_error
from constants.error_codes import ERROR_CODES
import config

class TestAirtableClient(unittest.TestCase):

    def setUp(self):
        """
        Initialize variables or set up any necessary database connections.
        This method will be executed before each test in the class.
        """
        self.mock_api_key = "mock_api_key"  # This is a mock API key for testing purposes
        self.airtable_client = AirtableClient(self.mock_api_key)

    def tearDown(self):
        """
        Close database connections and clean up any changes.
        This method will be executed after each test in the class.
        """
        pass

    def test_init_method(self):
        """
        Test if AirtableClient is initialized properly.
        """
        try:
            # Arrange
            expected_api_key = self.mock_api_key
            expected_base_id = config.AIRTABLE_BASE_ID  # Replace with the actual Base ID from your config
            
            # Act
            airtable_client = AirtableClient(expected_api_key)
            
            # Assert
            self.assertEqual(airtable_client.api.api_key, expected_api_key)
            self.assertEqual(airtable_client.active_baseID, expected_base_id)
            
        except Exception as e:
            error_message, http_status = handle_error('TEST001')
            self.fail(f"{error_message} | HTTP Status: {http_status} | Exception: {str(e)}")

    def get_methods(self):
        """Return methods available in AirtableClient.
        ---
        Debug Tag: DT.6.2-AirtableClient-GetMethods
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.6.2-AirtableClient-GetMethods | Time: {timestamp}")

        try:
            return get_methods(self)
        except Exception as e:
            error_message, http_status = handle_error('TEST001')
            logging.error(f"{error_message} | HTTP Status: {http_status} | Exception: {e}")
            return {}
    
if __name__ == '__main__':
    unittest.main()