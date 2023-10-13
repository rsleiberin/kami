from datetime import datetime
import logging
from modules.utils.utils import get_methods
from constants.error_codes import ERROR_CODES
from modules.utils.error_handler import handle_error

class FunctionState:
    """
    Maintains a state to track the last function that was invoked 
    and its arguments to avoid repetitive function calls.
    ---
    Debug Tag: DT.5-FunctionState
    """
    
    def __init__(self):
        """
        Initialize with default empty state for function and arguments.
        ---
        Debug Tag: DT.5.0-FunctionState-__init__
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.5.0-FunctionState-__init__ | Time: {timestamp}")
        
        try:
            self.last_function = None
            self.last_arguments = None
        except Exception as e:
            error_message, http_status = handle_error('FS001')
            logging.error(f"{error_message} | HTTP Status: {http_status} | Exception: {e}")

    def set(self, function_name, arguments):
        """
        Set the state with the provided function name and arguments.
        ---
        Debug Tag: DT.5.1-FunctionState-set
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.5.1-FunctionState-set | Time: {timestamp}")

        try:
            self.last_function = function_name
            self.last_arguments = arguments
        except Exception as e:
            error_message, http_status = handle_error('FS002')
            logging.error(f"{error_message} | HTTP Status: {http_status} | Exception: {e}")

    def check_repetition(self, function_name, arguments):
        """
        Check if the provided function name and arguments are the same 
        as the last invocation.
        ---
        Debug Tag: DT.5.2-FunctionState-check_repetition
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.5.2-FunctionState-check_repetition | Time: {timestamp}")

        try:
            return self.last_function == function_name and self.last_arguments == arguments
        except Exception as e:
            error_message, http_status = handle_error('FS003')
            logging.error(f"{error_message} | HTTP Status: {http_status} | Exception: {e}")
            return False

    @staticmethod
    def get_methods():
        """
        Return all the methods available in the FunctionState class.
        ---
        Debug Tag: DT.5.3-FunctionState-get_methods
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.5.3-FunctionState-get_methods | Time: {timestamp}")

        try:
            return get_methods(FunctionState)
        except Exception as e:
            error_message, http_status = handle_error('FS004')
            logging.error(f"{error_message} | HTTP Status: {http_status} | Exception: {e}")
            return {}
