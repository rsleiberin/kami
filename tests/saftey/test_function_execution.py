import unittest
from unittest import mock
from safety.function_execution import execute_function

class TestFunctionExecution(unittest.TestCase):
    
    def test_execute_function(self):
        """
        Test the execute_function method.
        """
        with mock.patch('safety.function_execution.print_tracer') as mock_print_tracer:
            # Mocking print_tracer to not output during tests
            user_id = 'test_user'
            func_call = 'TestFunction'
            
            result = execute_function(func_call, user_id)
            
            self.assertEqual(result, "Function Executed")
            mock_print_tracer.assert_called()

if __name__ == '__main__':
    unittest.main()
