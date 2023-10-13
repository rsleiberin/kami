import unittest
from constants.error_codes import ERROR_CODES
from modules.utils.error_handler import handle_error

class TestErrorHandler(unittest.TestCase):

    def setUp(self):
        """
        Initialize variables or set up any necessary database connections.
        This method will be executed before each test in the class.
        """
        self.valid_error_code = 'GEN001'
        self.invalid_error_code = 'INVALID_CODE'

    def tearDown(self):
        """
        Close database connections and clean up any changes.
        This method will be executed after each test in the class.
        """
        pass

    def test_handle_error_valid_code(self):
        """
        Test if handle_error returns the correct message and status code for a valid error code.
        """
        try:
            # Arrange
            expected_message = ERROR_CODES[self.valid_error_code]['message']
            expected_status = ERROR_CODES[self.valid_error_code]['http_status']
            
            # Act
            actual_message, actual_status = handle_error(self.valid_error_code)
            
            # Assert
            self.assertEqual(expected_message, actual_message)
            self.assertEqual(expected_status, actual_status)
            
        except Exception as e:
            self.fail(f"Test failed: {str(e)}")

    def test_handle_error_invalid_code(self):
        """
        Test if handle_error returns the generic message and status code for an invalid error code.
        """
        try:
            # Arrange
            expected_message = ERROR_CODES['GEN001']['message']
            expected_status = ERROR_CODES['GEN001']['http_status']
            
            # Act
            actual_message, actual_status = handle_error(self.invalid_error_code)
            
            # Assert
            self.assertEqual(expected_message, actual_message)
            self.assertEqual(expected_status, actual_status)
            
        except Exception as e:
            self.fail(f"Test failed: {str(e)}")

if __name__ == '__main__':
    unittest.main()
