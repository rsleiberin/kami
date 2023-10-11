import logging
from modules.utils.utils import get_methods

class FunctionState:
    """
    Maintains a state to track the last function that was invoked 
    and its arguments to avoid repetitive function calls.
    """
    
    def __init__(self):
        """Initialize with default empty state for function and arguments."""
        self.last_function = None
        self.last_arguments = None

    def set(self, function_name, arguments):
        """
        Set the state with the provided function name and arguments.

        Parameters:
        - function_name (str): Name of the function.
        - arguments (dict): Arguments passed to the function.
        """
        self.last_function = function_name
        self.last_arguments = arguments

    def check_repetition(self, function_name, arguments):
        """
        Check if the provided function name and arguments are the same 
        as the last invocation.

        Parameters:
        - function_name (str): Name of the function.
        - arguments (dict): Arguments passed to the function.

        Returns:
        bool: True if it's a repeated call, False otherwise.
        """
        return self.last_function == function_name and self.last_arguments == arguments

    @staticmethod
    def get_methods():
        """Return all the methods available in the FunctionState class."""
        try:
            return get_methods(FunctionState)
        except Exception as e:
            logging.error(str(e))