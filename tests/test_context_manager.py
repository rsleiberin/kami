import unittest
from unittest.mock import patch, MagicMock, call
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
    
    @patch('context_management.context_manager.print_tracer')  # Mock the print_tracer method
    @patch('context_management.context_manager.UserInputAnalysisSocket')  # Mock the UserInputAnalysisSocket class
    def test_capture_and_analyze_user_input(self, MockUserInputAnalysisSocket, mock_print_tracer):
        # Create mock instances and set return values
        mock_socket_instance = MockUserInputAnalysisSocket.return_value
        mock_socket_instance.capture_user_input.return_value = "Test Input"
        mock_socket_instance.analyze.return_value = "Test Intent"

        # Create an instance of ContextManager and call the method
        cm = ContextManager()
        cm.capture_and_analyze_user_input()

        # Validate the context buffer
        self.assertEqual(cm.context_buffer[-1], {"UserInput": "Test Input", "Intent": "Test Intent"})

    @patch('context_management.context_manager.print_tracer')  # Mock the print_tracer method
    @patch('context_management.context_manager.RequirementMappingSocket')  # Mock the RequirementMappingSocket class
    def test_map_requirements_based_on_intent(self, MockRequirementMappingSocket, mock_print_tracer):
        # Create mock instances and set return values
        mock_socket_instance = MockRequirementMappingSocket.return_value
        mock_socket_instance.map.return_value = {"Requirement1": "Value1", "Requirement2": "Value2"}
        
        # Create an instance of ContextManager and call the method
        cm = ContextManager()
        cm.map_requirements_based_on_intent("TestIntent")

        # Validate the context buffer
        self.assertEqual(cm.context_buffer[-1], {"Intent": "TestIntent", "Requirements": {"Requirement1": "Value1", "Requirement2": "Value2"}})

    @patch('context_management.context_manager.print_tracer')  # Mock the print_tracer method
    @patch('context_management.context_manager.SubAgentRegistry')  # Mock the SubAgentRegistry class
    def test_register_agent(self, MockSubAgentRegistry, mock_print_tracer):
        # Create mock instances and set return values
        mock_registry_instance = MockSubAgentRegistry.return_value
        mock_registry_instance.register.return_value = True  # Simulating successful registration
        
        # Create an instance of ContextManager and call the method
        cm = ContextManager()
        cm.register_agent("TestAgent")

        # Validate the context buffer
        self.assertEqual(cm.context_buffer[-1], {"Action": "Registered", "Agent": "TestAgent"})

    @patch('context_management.context_manager.print_tracer')  # Mock the print_tracer method
    @patch('context_management.context_manager.SubAgentRegistry')  # Mock the SubAgentRegistry class
    def test_register_sub_agent(self, MockSubAgentRegistry, mock_print_tracer):
        # Create mock instances and set return values
        mock_registry_instance = MockSubAgentRegistry.return_value
        mock_registry_instance.register.return_value = True  # Simulating successful registration
        
        # Create an instance of ContextManager and call the method
        cm = ContextManager()
        cm.register_sub_agent("TestSubAgent")

        # Validate the context buffer
        self.assertEqual(cm.context_buffer[-1], {"Action": "Registered", "SubAgent": "TestSubAgent"})

    @patch('context_management.context_manager.print_tracer')  # Mock the print_tracer method
    @patch('context_management.context_manager.SubAgentRegistry')  # Mock the SubAgentRegistry class
    def test_get_active_sub_agents(self, MockSubAgentRegistry, mock_print_tracer):
        # Create mock instances and set return values
        mock_registry_instance = MockSubAgentRegistry.return_value
        mock_registry_instance.get_active_agents.return_value = ["Agent1", "Agent2"]  # Simulating existing agents
        
        # Create an instance of ContextManager and call the method
        cm = ContextManager()
        cm.get_active_sub_agents()

        # Validate the context buffer
        self.assertEqual(cm.context_buffer[-1], {"Action": "Fetched", "ActiveSubAgents": ["Agent1", "Agent2"]})

    @patch('context_management.context_manager.print_tracer')  # Mock the print_tracer method
    def test_manage_token_limit(self, mock_print_tracer):
        # Create an instance of ContextManager
        cm = ContextManager()

        # Call the manage_token_limit method
        cm.manage_token_limit()

        # Check if the print_tracer was called with the correct parameters
        mock_print_tracer.assert_any_call("ContextManager", "manage_token_limit", "Start")
        mock_print_tracer.assert_any_call("ContextManager", "manage_token_limit", "Event", "Token management logic to be implemented.")
        mock_print_tracer.assert_any_call("ContextManager", "manage_token_limit", "End")

    @patch('context_management.context_manager.print_tracer')  # Mock the print_tracer method
    def test_get_context(self, mock_print_tracer):
        # Create an instance of ContextManager
        cm = ContextManager()
        
        # Populate the context buffer with some dummy data
        cm.context_buffer = [{'some': 'context'}, {'more': 'context'}]
        
        # Call the method to test
        returned_context = cm.get_context()
        
        # Check if print_tracer was called with the correct parameters
        mock_print_tracer.assert_any_call("ContextManager", "get_context", "Start")
        mock_print_tracer.assert_any_call("ContextManager", "get_context", "End")
        
        # Further assertions related to the method's behavior (like checking returned context)
        self.assertEqual(returned_context, cm.context_buffer)

    @patch('context_management.context_manager.print_tracer')
    def test_activate_socket(self, mock_print_tracer):
        cm = ContextManager()
        mock_socket_instance = MagicMock()
        cm.activate_socket('MockSocket', mock_socket_instance)
        
        print("Debug: Mock print_tracer calls:", mock_print_tracer.call_args_list)  # Debug statement
        
        mock_print_tracer.assert_any_call("ContextManager", "activate_socket", "Start", f"Activating socket: MockSocket")
        mock_print_tracer.assert_any_call("ContextManager", "activate_socket", "End")
        self.assertEqual(cm.active_sockets.get('MockSocket'), mock_socket_instance)

    from unittest.mock import call  # Add this import at the top of your test file if it's not already there

    @patch('context_management.context_manager.print_tracer')  # Mock the print_tracer method
    def test_deactivate_socket(self, mock_print_tracer):
        # Create an instance of ContextManager
        cm = ContextManager()
        
        # Create a mock socket instance and activate it
        mock_socket_instance = MagicMock()
        cm.activate_socket('MockSocket', mock_socket_instance)
        
        # Debug print
        print("Debug: Inside deactivate_socket")
        
        # Call the method to test
        cm.deactivate_socket('MockSocket')
        
        # Debug print to show what print_tracer was called with
        print(f"Debug: Mock print_tracer calls: {mock_print_tracer.call_args_list}")
        
        # Explicitly check the call_args_list
        self.assertIn(call("ContextManager", "deactivate_socket", "Start", "Deactivating socket: MockSocket"), mock_print_tracer.call_args_list)
        self.assertIn(call("ContextManager", "deactivate_socket", "End"), mock_print_tracer.call_args_list)
        
        # Further assertions related to the method's behavior (like checking if the socket is deactivated)
        self.assertIsNone(cm.active_sockets.get('MockSocket'))
    
    @patch('context_management.context_manager.print_tracer')  # Mock the print_tracer method
    def test_get_context_for_LLMSwitcher(self, mock_print_tracer):
        # Create an instance of ContextManager
        cm = ContextManager()
        
        # Setup a mock context_buffer for this instance
        mock_context_buffer = {'some': 'context'}
        cm.context_buffer = mock_context_buffer
        
        # Call the method to test
        returned_context = cm.get_context_for_LLMSwitcher()
        
        # Check if print_tracer was called with the correct parameters
        mock_print_tracer.assert_any_call("ContextManager", "get_context_for_LLMSwitcher", "Start")
        mock_print_tracer.assert_any_call("ContextManager", "get_context_for_LLMSwitcher", "End")
        
        # Further assertions related to the method's behavior (like checking if the context is returned correctly)
        self.assertEqual(returned_context, mock_context_buffer)

    @patch('context_management.context_manager.print_tracer')  # Mock the print_tracer method
    def test_clear_context(self, mock_print_tracer):
        # Create an instance of ContextManager
        cm = ContextManager()
        
        # Populate the context buffer with some data
        cm.context_buffer = {'key': 'value'}
        
        # Call the method to test
        cm.clear_context()
        
        # Check if print_tracer was called with the correct parameters
        mock_print_tracer.assert_any_call("ContextManager", "clear_context", "Start")
        mock_print_tracer.assert_any_call("ContextManager", "clear_context", "Event", "Context buffer cleared.")
        mock_print_tracer.assert_any_call("ContextManager", "clear_context", "End")
        
        # Further assertions to ensure the context buffer is actually cleared
        self.assertEqual(cm.context_buffer, {})

    @patch('context_management.context_manager.print_tracer')  # Mock the print_tracer method
    def test_update_token_limit(self, mock_print_tracer):
        # Create an instance of ContextManager
        cm = ContextManager()
        
        # Define a new token limit
        new_limit = 2000
        
        # Call the method to test
        cm.update_token_limit(new_limit)
        
        # Check if print_tracer was called with the correct parameters
        mock_print_tracer.assert_any_call("ContextManager", "update_token_limit", "Start", f"New limit: {new_limit}")
        mock_print_tracer.assert_any_call("ContextManager", "update_token_limit", "Event", f"Token limit updated to {new_limit}.")
        mock_print_tracer.assert_any_call("ContextManager", "update_token_limit", "End")
        
        # Further assertions to ensure the token limit is actually updated
        self.assertEqual(cm.token_limit, new_limit)

    @patch('context_management.context_manager.print_tracer')  # Mock the print_tracer method
    def test_save_context(self, mock_print_tracer):
        # Create an instance of ContextManager
        cm = ContextManager()
        
        # Call the method to test
        cm.save_context()
        
        # Check if print_tracer was called with the correct parameters
        mock_print_tracer.assert_any_call("ContextManager", "save_context", "Start")
        mock_print_tracer.assert_any_call("ContextManager", "save_context", "Event", "Context saved successfully.")
        mock_print_tracer.assert_any_call("ContextManager", "save_context", "End")

    @patch('context_management.context_manager.print_tracer')  # Mock the print_tracer method
    @patch('context_management.context_manager.FeedbackSocket.collect_initial_feedback')  # Mock the collect_initial_feedback method
    def test_collect_feedback(self, mock_collect_initial_feedback, mock_print_tracer):
        # Create an instance of ContextManager
        cm = ContextManager()
        
        # Mock the feedback data
        mock_collect_initial_feedback.return_value = {'some': 'feedback'}
        
        # Call the method to test
        cm.collect_feedback()
        
        # Check if print_tracer was called with the correct parameters
        mock_print_tracer.assert_any_call("ContextManager", "collect_feedback", "Start")
        mock_print_tracer.assert_any_call("ContextManager", "collect_feedback", "Event", "Feedback collected successfully.")
        mock_print_tracer.assert_any_call("ContextManager", "collect_feedback", "End")

    @patch('context_management.context_manager.print_tracer')  # Mock the print_tracer method
    @patch('context_management.context_manager.FeedbackSocket.indicates_issues_or_improvements')  # Mock the indicates_issues_or_improvements method
    def test_check_feedback_for_issues(self, mock_indicates_issues_or_improvements, mock_print_tracer):
        # Create an instance of ContextManager
        cm = ContextManager()
        
        # Mock the feedback data and method
        cm.context_buffer.append({"Feedback": {'some': 'feedback'}})
        mock_indicates_issues_or_improvements.return_value = True
        
        # Call the method to test
        cm.check_feedback_for_issues()
        
        # Check if print_tracer was called with the correct parameters
        mock_print_tracer.assert_any_call("ContextManager", "check_feedback_for_issues", "Start")
        mock_print_tracer.assert_any_call("ContextManager", "check_feedback_for_issues", "Event", "Issues or improvements detected.")
        mock_print_tracer.assert_any_call("ContextManager", "check_feedback_for_issues", "End")

if __name__ == "__main__":
    unittest.main()