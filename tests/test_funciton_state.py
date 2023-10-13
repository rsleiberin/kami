import unittest
from modules.llm_interface.function_state import FunctionState
from constants.error_codes import ERROR_CODES
from modules.utils.error_handler import handle_error

class TestFunctionState(unittest.TestCase):

    def setUp(self):
        """
        Setup FunctionState object before each test.
        ---
        Debug Tag: DT.5.Test-FunctionState-setUp
        """
        self.func_state = FunctionState()
        
    def tearDown(self):
        """
        Cleanup after each test.
        ---
        Debug Tag: DT.5.Test-FunctionState-tearDown
        """
        self.func_state = None
    def test_init(self):
        """
        Test if the FunctionState class is initialized correctly.
        ---
        Debug Tag: DT.5.Test.1-FunctionState-test_init
        """
        try:
            # Assert
            self.assertIsNone(self.func_state.last_function)
            self.assertIsNone(self.func_state.last_arguments)
        except Exception as e:
            self.fail(f"Test failed: {str(e)}")

    def test_set(self):
        """
        Test if the set method correctly sets last_function and last_arguments.
        ---
        Debug Tag: DT.5.Test.2-FunctionState-test_set
        """
        try:
            # Act
            self.func_state.set("some_function", {"arg1": 1})
            
            # Assert
            self.assertEqual(self.func_state.last_function, "some_function")
            self.assertEqual(self.func_state.last_arguments, {"arg1": 1})
        except Exception as e:
            self.fail(f"Test failed: {str(e)}")

    def test_check_repetition(self):
        """
        Test if the check_repetition method correctly identifies repeated function calls.
        ---
        Debug Tag: DT.5.Test.3-FunctionState-test_check_repetition
        """
        try:
            # Setup
            self.func_state.set("some_function", {"arg1": 1})
            
            # Act & Assert
            self.assertTrue(self.func_state.check_repetition("some_function", {"arg1": 1}))
            self.assertFalse(self.func_state.check_repetition("other_function", {"arg1": 1}))
        except Exception as e:
            self.fail(f"Test failed: {str(e)}")

    def test_get_methods(self):
        """
        Test if get_methods returns the correct set of method names.
        ---
        Debug Tag: DT.5.Test.4-FunctionState-test_get_methods
        """
        try:
            # Act
            methods = FunctionState.get_methods()
            
            # Assert
            self.assertIn("set", methods)
            self.assertIn("check_repetition", methods)
            self.assertIn("get_methods", methods)
        except Exception as e:
            self.fail(f"Test failed: {str(e)}")

if __name__ == '__main__':
    unittest.main()

