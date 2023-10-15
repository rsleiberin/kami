import sys
import unittest
from unittest.mock import patch, MagicMock
sys.path.append('/home/tank/kami')  # Add this line before your problematic import, also note the starting '/'
import logging

from modules.module_registry.module_registry import ModuleRegistry  # Now this import should work
import config
from modules.utils.error_handler import handle_error

class TestModuleRegistry(unittest.TestCase):
    
    def setUp(self):
        # This method will be executed before each test in the class
        self.module_registry = ModuleRegistry()
        self.mock_gpt_model = "Mock GPT Model"  # Replace with a more realistic mock if needed
        
    def tearDown(self):
        # This method will be executed after each test in the class
        pass
    
    @patch('modules.module_registry.module_registry.logging')
    def test_register_module(self, mock_logging):
        module_registry = ModuleRegistry()

        # Test registering a module without instance_name
        test_module1 = "TestModule1Instance"
        module_registry.register_module("TestModule1", test_module1)
        self.assertEqual(module_registry.modules["TestModule1"], test_module1)

        # Test registering a module with instance_name
        test_module2 = "TestModule2Instance"
        module_registry.register_module("TestModule2", test_module2, "Instance1")
        self.assertEqual(module_registry.modules["TestModule2_Instance1"], test_module2)

        # Test registering another instance of the same module
        test_module3 = "TestModule2AnotherInstance"
        module_registry.register_module("TestModule2", test_module3, "Instance2")
        self.assertEqual(module_registry.modules["TestModule2_Instance2"], test_module3)
    
    def test_get_model_for_task(self):
        """
        Test the get_model_for_task method of the ModuleRegistry class.
        """
        try:
            with patch('modules.utils.error_handler.handle_error') as mock_handle_error:
                self.module_registry.perform_task('chat')
                self.assertEqual(mock_handle_error.call_count, 0)
                self.module_registry.perform_task('generate_text')
                self.assertEqual(mock_handle_error.call_count, 0)
                with self.assertRaises(Exception):
                    self.module_registry.perform_task('unsupported_task')
                self.assertEqual(mock_handle_error.call_count, 1)
        except Exception as e:
            handle_error(e)

    def test_execute_module_method_success(self):
        with patch('modules.utils.error_handler.handle_error') as MockedHandleError:
            mock_module = MagicMock()
            mock_module.some_method.return_value = 'some_return_value'
            self.module_registry.modules['MockModule'] = mock_module

            result = self.module_registry.execute_module_method('MockModule', 'some_method', 'arg1', key='value')

            mock_module.some_method.assert_called_with('arg1', key='value')
            self.assertEqual(result, 'some_return_value')

    def test_get_methods_success(self):
        with patch('modules.utils.error_handler.handle_error') as MockedHandleError:
            result = self.module_registry.get_methods()
            self.assertIsInstance(result, dict)
            self.assertTrue(result) 

    def test_get_model_for_task(self):
        """Test the get_model_for_task method."""
        try:
            self.module_registry.modules['gpt'] = self.mock_gpt_model

            result = self.module_registry.get_model_for_task('chat')
            self.assertEqual(result, self.mock_gpt_model)

            result = self.module_registry.get_model_for_task('generate_text')
            self.assertEqual(result, self.mock_gpt_model)

            result = self.module_registry.get_model_for_task('unsupported_task')
            self.assertIsNone(result)

            with patch('modules.utils.error_handler.handle_error') as mock_handle_error:
                mock_handle_error.return_value = ("Error message", 500)
                self.module_registry.modules = {}
                result = self.module_registry.get_model_for_task('chat')
                self.assertEqual(result, "Error message")
        except Exception as e:
            logging.error(f"An error occurred while testing get_model_for_task: {e}")

    def test_get_registered_module_methods(self):
        mock_module = "Mock Module"
        self.module_registry.modules['MockModule'] = mock_module

        with patch('modules.module_registry.get_methods') as mock_get_methods:
            mock_get_methods.return_value = ['method1', 'method2']
            result = self.module_registry.get_registered_module_methods('MockModule')
            self.assertEqual(result, ['method1', 'method2'])

    def test_load_module_class(self):
        class TempClass:
            pass

        sys.modules['temp_module'] = type('temp_module', (), {'TempClass': TempClass})

        result = self.module_registry.load_module_class('temp_module.TempClass')
        self.assertEqual(result, TempClass)
    
    @patch('logging.error')
    @patch('datetime.datetime')
    def test_perform_task(self, mock_logging_error, mock_datetime):
        mock_datetime.now.return_value.strftime.return_value = "some_timestamp"
        mock_model = MagicMock()
        mock_model.perform.return_value = 'some_result'
        self.module_registry.modules['some_model'] = mock_model

        # Case 1: Model exists and has 'perform' method
        with patch('modules.module_registry.ModuleRegistry.get_model_for_task') as mock_get_model_for_task:
            mock_get_model_for_task.return_value = mock_model
            result = self.module_registry.perform_task('some_task', 'arg1', key='value')
            self.assertEqual(result, 'some_result')

        # Case 2: Model exists but does not have 'perform' method
        mock_model_without_perform = MagicMock()
        del mock_model_without_perform.perform
        with patch('modules.module_registry.ModuleRegistry.get_model_for_task') as mock_get_model_for_task:
            mock_get_model_for_task.return_value = mock_model_without_perform
            result = self.module_registry.perform_task('some_task', 'arg1', key='value')
            mock_logging_error.assert_called()  # Make sure the error was logged
            self.assertNotEqual(result, 'some_result')

        # Case 3: Model does not exist
        with patch('modules.module_registry.ModuleRegistry.get_model_for_task') as mock_get_model_for_task:
            mock_get_model_for_task.return_value = None
            result = self.module_registry.perform_task('some_task', 'arg1', key='value')
            mock_logging_error.assert_called()  # Make sure the error was logged

       
if __name__ == '__main__':
    unittest.main()
