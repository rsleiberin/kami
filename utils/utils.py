import inspect
from constants.error_codes import ERROR_CODES

#use this in any class as the following: print_tracer("ModuleRegistry", "__init__", "Start")
#Later on we will add custom print tracer paths where we can turn on and off modules and individual functions for streamlined context.
def print_tracer(module_name, method_name, event, additional_info=""):
    """
    Print standardized tracers for debugging and context.
    
    Args:
    - module_name (str): The name of the module or class.
    - method_name (str): The method where the tracer is being called.
    - event (str): A short descriptor of the event or step.
    - additional_info (str, optional): Any additional information or context.
    """
    tracer = f"[{module_name}][{method_name}][{event}] {additional_info}"
    print(tracer)

def get_methods(obj):
    """
    Gets all the methods available in the class and their information.
    Returns a dictionary with method names as keys and method details as values.
    
    :param obj: The object whose methods need to be fetched.
    :return: A dictionary containing method details or None if an error occurs.
    """
    class_name = obj.__class__.__name__
    print_tracer("Utils", "get_methods", "Start", f"Inspecting {class_name}")

    method_list = {}

    try:
        for name, data in inspect.getmembers(obj, predicate=inspect.ismethod):
            if name.startswith("__"):
                continue
            
            print_tracer("Utils", "get_methods", "MethodFound", name)

            args = [a for a in inspect.getfullargspec(data).args if a != "self"]
            docstring = str(data.__doc__).strip() if data.__doc__ else "No documentation provided."
            method_list[name] = {"args": args, "doc": docstring}

        print_tracer("Utils", "get_methods", "End", f"Completed inspecting {class_name}")
        return method_list
    except Exception as e:
        print_tracer("Utils", "get_methods", "Error", f"An error occurred: {str(e)}")
        # We can expand this section later with specific error handling logic if needed.
        return None

def add_error_codes(new_codes: dict):
    """
    Add new error codes to the centralized error code dictionary.

    Args:
    - new_codes (dict): Dictionary of new error codes and their details.
    """
    from constants import error_codes  # Importing here to avoid circular imports
    error_codes.ERROR_CODES.update(new_codes)

def handle_error(error_code: str):
    """
    Fetches the appropriate message, HTTP status code, severity, description, and resolution for a given error code.
    """
    print_trace("Utils", "handle_error", f"Retrieving error details for code {error_code}")
    
    try:
        error_info = ERROR_CODES.get(error_code, ERROR_CODES['GEN001'])
        print_trace("Utils", "handle_error", f"Error details retrieved successfully for code {error_code}")
        return error_info
    except Exception as e:
        # Fallback if there's an issue retrieving the error info
        print_trace("Utils", "handle_error", f"Error encountered while retrieving error details for code {error_code}")
        return {
            'message': f"Error in handle_error: {str(e)}",
            'http_status': 500,
            'severity': 'ERROR',
            'description': 'An error occurred while handling another error.',
            'resolution': 'Check the traceback for more details.',
        }




