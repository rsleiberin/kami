from datetime import datetime
import logging
from modules.utils.error_handler import handle_error
from modules.utils.utils import get_methods 

logging.basicConfig(level=logging.DEBUG)

class ContextManager:
    def __init__(self, initial_context=None):
        """
        Initialize the Context Manager with an empty context or a given context.
        ---
        Debug Tag: DT.X-ContextManager-Initialization
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.X-ContextManager-Initialization | Time: {timestamp}")

        try:
            self.current_context = initial_context if initial_context is not None else {}
        except Exception as e:
            error_message, http_status = handle_error('CTXMGR001')  # You will need to define this error code
            logging.error(f"{error_message} | HTTP Status: {http_status} | Exception: {e}")
            raise  # Re-raise the exception to ensure it gets caught higher up
    def get_context(self):
        """
        Retrieve current context.
        ---
        Debug Tag: DT.5.1-ContextManager-get_context
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.5.1-ContextManager-get_context | Time: {timestamp}")

        try:
            return self.current_context
        except Exception as e:
            error_message, http_status = handle_error('CONTEXT002')
            logging.error(f"{error_message} | HTTP Status: {http_status} | Exception: {e}")
            return None

    def set_context(self, new_context):
        """
        Set the current context.
        ---
        Debug Tag: DT.5.2-ContextManager-set_context
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.5.2-ContextManager-set_context | Time: {timestamp}")

        try:
            if not isinstance(new_context, dict):
                raise ValueError("new_context must be a dictionary.")
            self.current_context = new_context
            return True
        except Exception as e:
            error_message, http_status = handle_error('CONTEXT003')
            logging.error(f"{error_message} | HTTP Status: {http_status} | Exception: {e}")
            return False

    def update_context(self, update_values):
        """
        Update the current context based on new data.
        ---
        Debug Tag: DT.12.1-ContextManager-update_context
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.12.1-ContextManager-update_context | Time: {timestamp}")

        try:
            self.current_context.update(update_values)
        except Exception as e:
            error_message, http_status = handle_error('CONTEXT002')
            logging.error(f"{error_message} | HTTP Status: {http_status} | Exception: {e}")

    def get_methods(self):
        """
        Retrieve the available methods in this class.
        ---
        Debug Tag: DT.X.1-ContextManager-get_methods
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.X.1-ContextManager-get_methods | Time: {timestamp}")

        try:
            return get_methods(self)
        except Exception as e:
            error_message, http_status = handle_error('CTXMGR002')  # You will need to define this error code
            logging.error(f"{error_message} | HTTP Status: {http_status} | Exception: {e}")
            return None