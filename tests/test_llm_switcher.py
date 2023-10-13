import unittest
from unittest.mock import patch, MagicMock
from modules.llm_interface.llm_switcher import LLMSwitcher  # Make sure the import is correct
import importlib

class TestLLMSwitcher(unittest.TestCase):

    def setUp(self):
        """
        Set up mock objects and instance for each test case.
        """
        self.mock_airtable_client = patch('modules.databases.airtable_client.airtable_client.AirtableClient.__init__').start()
        self.mock_airtable_client.return_value = None  # Simulate no return
        
        self.mock_chat_gpt = patch('modules.llm_interface.chat_gpt.chat_gpt.ChatGPT.__init__').start()
        self.mock_chat_gpt.return_value = None  # Simulate no return

        self.llm_switcher = LLMSwitcher()

    def tearDown(self):
        """
        Clean up mock objects after each test case.
        """
        patch.stopall()

    def test_init(self):
        """
        Test if the LLMSwitcher class is initialized correctly.
        """
        try:
            # Assert
            self.assertIsNotNone(self.llm_switcher.modules)
        except Exception as e:
            self.fail(f"Test failed: {str(e)}")

    def test_get_methods(self):
        """
        Test if get_methods returns methods for the LLMSwitcher class.
        """
        try:
            # Act
            methods = self.llm_switcher.get_methods()

            # Assert
            self.assertIsNotNone(methods)
            self.assertTrue('get_methods' in methods)
        except Exception as e:
            self.fail(f"Test failed: {str(e)}")
    
    def test_register_module(self):
        """
        Test if register_module correctly registers a new module.
        """
        try:
            # Arrange
            mock_module = MagicMock()  # Create a mock module instance
            module_name = "MockModule"

            # Act
            self.llm_switcher.register_module(module_name, mock_module)

            # Assert
            self.assertIn(module_name, self.llm_switcher.modules)
            self.assertIs(self.llm_switcher.modules[module_name], mock_module)
            
            print(f"Test for registering {module_name} passed.")

        except Exception as e:
            self.fail(f"Test failed: {str(e)}")

    def test_execute_module_method(self):
        """
        Test if execute_module_method correctly calls a method from a registered module.
        """
        try:
            # Arrange
            mock_module = MagicMock()
            mock_method = MagicMock(return_value="mock_return_value")
            mock_module.mock_method = mock_method
            self.llm_switcher.register_module("MockModule", mock_module)
            
            module_name = "MockModule"
            method_code = "mock_method"
            
            # Act
            result = self.llm_switcher.execute_module_method(module_name, method_code)
            
            # Assert
            mock_method.assert_called_once()
            self.assertEqual(result, "mock_return_value")
            
            print(f"Test for executing method {method_code} from {module_name} passed.")

        except Exception as e:
            self.fail(f"Test failed: {str(e)}")

    def test_execute_module_method(self):
        """
        Test if execute_module_method correctly calls a method from a registered module.
        """
        try:
            # Arrange
            mock_module = MagicMock()
            mock_method = MagicMock(return_value="mock_return_value")
            mock_module.mock_method = mock_method
            self.llm_switcher.register_module("MockModule", mock_module)
            
            module_name = "MockModule"
            method_code = "mock_method"
            
            # Act
            result = self.llm_switcher.execute_module_method(module_name, method_code)
            
            # Assert
            mock_method.assert_called_once()
            self.assertEqual(result, "mock_return_value")
            
            print(f"Test for executing method {method_code} from {module_name} passed.")

        except Exception as e:
            self.fail(f"Test failed: {str(e)}")

    def test_get_registered_module_methods(self):
        """
        Test if get_registered_module_methods correctly fetches the methods of a registered module.
        """
        try:
            # Arrange
            mock_module = MagicMock()
            mock_module.mock_method_one = MagicMock()
            mock_module.mock_method_two = MagicMock()
            self.llm_switcher.register_module("MockModule", mock_module)
            
            module_name = "MockModule"
            
            # Act
            methods = self.llm_switcher.get_registered_module_methods(module_name)
            
            # Assert
            self.assertTrue('mock_method_one' in methods)
            self.assertTrue('mock_method_two' in methods)
            
            print(f"Test for getting registered module methods for {module_name} passed.")

        except Exception as e:
            self.fail(f"Test failed: {str(e)}")
    
    def test_get_model_for_task(self):
        """
        Test if get_model_for_task correctly selects the appropriate LLM for a given task.
        """
        try:
            # Arrange
            mock_gpt = MagicMock()
            self.llm_switcher.gpt = mock_gpt
            
            tasks_with_gpt = ["chat", "generate_text"]
            task_without_gpt = "image_recognition"
            
            # Act & Assert for tasks that should use GPT
            for task in tasks_with_gpt:
                selected_model = self.llm_switcher.get_model_for_task(task)
                self.assertEqual(selected_model, mock_gpt, f"For task {task}, selected model should be GPT.")
            
            # Act & Assert for tasks that should not use GPT
            selected_model = self.llm_switcher.get_model_for_task(task_without_gpt)
            self.assertIsNone(selected_model, f"For task {task_without_gpt}, selected model should be None.")
            
            print("Test for getting the model for a task passed.")

        except Exception as e:
            self.fail(f"Test failed: {str(e)}")

    def test_perform_task(self):
        """
        Test if perform_task correctly uses the best-suited LLM to perform a given task.
        """
        try:
            # Arrange
            mock_gpt = MagicMock()
            mock_gpt.perform = MagicMock(return_value="Hello, world!")
            
            self.llm_switcher.gpt = mock_gpt
            
            # Task that should use GPT and have the perform method
            task_with_perform = "chat"
            
            # Act
            result = self.llm_switcher.perform_task(task_with_perform, "Hi!")
            
            # Assert
            mock_gpt.perform.assert_called_with(task_with_perform, "Hi!")
            self.assertEqual(result, "Hello, world!", f"Result for task {task_with_perform} should match the mock's return value.")
            
            print("Test for performing a task passed.")

        except Exception as e:
            self.fail(f"Test failed: {str(e)}")

    def test_load_module_class(self):
        """
        Test if load_module_class can dynamically import a class based on its full class string.
        """
        try:
            # Arrange
            valid_class_string = "datetime.datetime"
            invalid_module_string = "nonexistent_module.ClassName"
            invalid_class_string = "datetime.NonexistentClass"

            # Act & Assert for valid class string
            valid_result = self.llm_switcher.load_module_class(valid_class_string)
            self.assertEqual(valid_result, importlib.import_module('datetime').datetime, f"Result for {valid_class_string} should match the imported class.")

            # Act & Assert for invalid module string
            invalid_module_result = self.llm_switcher.load_module_class(invalid_module_string)
            self.assertIsNone(invalid_module_result, f"Result for {invalid_module_string} should be None.")

            # Act & Assert for invalid class string
            invalid_class_result = self.llm_switcher.load_module_class(invalid_class_string)
            self.assertIsNone(invalid_class_result, f"Result for {invalid_class_string} should be None.")

            print("Test for loading a module class passed.")

        except Exception as e:
            self.fail(f"Test failed: {str(e)}")

    def test_use_module(self):
        """
        Test if use_module can correctly execute a method from a registered module.
        """
        try:
            # Arrange
            class DummyModule:
                def hello(self, name):
                    return f"Hello, {name}"

            self.llm_switcher.register_module("Dummy", DummyModule())

            # Act & Assert for a valid method
            valid_result = self.llm_switcher.use_module("Dummy", "hello", name="John")
            self.assertEqual(valid_result, "Hello, John", "Result for valid method should match expected output.")

            # Act & Assert for an invalid module
            invalid_module_result = self.llm_switcher.use_module("NonexistentModule", "hello", name="John")
            self.assertIsInstance(invalid_module_result, str, "Result for an invalid module should be an error string.")

            # Act & Assert for an invalid method
            invalid_method_result = self.llm_switcher.use_module("Dummy", "nonexistent_method", name="John")
            self.assertIsInstance(invalid_method_result, str, "Result for an invalid method should be an error string.")

            # Act & Assert for a non-callable attribute
            self.llm_switcher.modules["Dummy"].non_callable = "I'm not callable"
            non_callable_result = self.llm_switcher.use_module("Dummy", "non_callable")
            self.assertIsInstance(non_callable_result, str, "Result for a non-callable attribute should be an error string.")

            print("Test for using a module method passed.")

        except Exception as e:
            self.fail(f"Test failed: {str(e)}")

if __name__ == '__main__':
    unittest.main()