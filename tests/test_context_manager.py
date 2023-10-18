import unittest
from unittest.mock import patch, MagicMock
from context_management.context_manager import ContextManager  # Import the ContextManager class from its module

class TestContextManager(unittest.TestCase):
    
    @patch('context_management.context_manager.print_tracer')  # Mock the print_tracer method
    def test_init_method(self, mock_print_tracer):
        # Create an instance of ContextManager
        cm = ContextManager()
        
        # Check if the print_tracer was called with the correct parameters
        mock_print_tracer.assert_any_call("ContextManager", "__init__", "Start")
        mock_print_tracer.assert_any_call("ContextManager", "__init__", "End")

    @patch('context_management.context_manager.print_tracer')  # Mock the print_tracer method
    def test_load_user_data(self, mock_print_tracer):
        # Create an instance of ContextManager
        cm = ContextManager()
        
        # Call load_user_data method
        cm.load_user_data()

        # Check if the print_tracer was called with the correct parameters
        mock_print_tracer.assert_any_call("ContextManager", "load_user_data", "Start")
        mock_print_tracer.assert_any_call("ContextManager", "load_user_data", "End")

    @patch('context_management.context_manager.print_tracer')  # Mock the print_tracer method
    def test_add_socket(self, mock_print_tracer):
        # Create an instance of ContextManager
        cm = ContextManager()

        # Call add_socket method
        cm.add_socket("TestSocket", "TestInstance")

        # Check if the print_tracer was called with the correct parameters
        mock_print_tracer.assert_any_call("ContextManager", "add_socket", "Start")
        mock_print_tracer.assert_any_call("ContextManager", "add_socket", "End")

    @patch('context_management.context_manager.print_tracer')  # Mock the print_tracer method
    def test_process_socket(self, mock_print_tracer):
        # Create an instance of ContextManager
        cm = ContextManager()
        mock_socket_instance = MagicMock()
        # Set up the mock to return some dummy context data
        mock_socket_instance.process.return_value = {'some': 'context'}
        
        # Call the method to test
        cm.active_sockets['MockSocket'] = mock_socket_instance

        cm.process_socket('MockSocket', mock_socket_instance)

        # Check if print_tracer was called with the correct parameters
        mock_print_tracer.assert_any_call("ContextManager", "process_socket", "Start")
        mock_print_tracer.assert_any_call("ContextManager", "process_socket", "End")

        # Further assertions related to the method's behavior (like checking context_buffer)
        if cm.context_buffer:
            self.assertEqual(cm.context_buffer[-1], {'some': 'context'})
        else:
            self.fail("Context buffer is empty.")


if __name__ == "__main__":
    unittest.main()