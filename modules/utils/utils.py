import inspect
import logging

def get_methods(obj):
    """Returns dictionary of method and class names, docstrings, and argument signatures."""
    try:
        methods = {}
        for func in dir(obj):
            attr = getattr(obj, func)
            if callable(attr) and not func.startswith("__"):
                methods[func] = {
                    'args': inspect.signature(attr).parameters.keys(),
                    'doc': attr.__doc__.split('\n')[0] if attr.__doc__ else ''
                }
            elif inspect.isclass(attr):
                methods[func] = {
                    'args': [],
                    'doc': attr.__doc__ if attr.__doc__ else ''
                }
        return methods
    except Exception as e:
        logging.error(str(e))
def get_module_info(module):
    """
    Retrieves and returns information about the module at the specified path.
    
    This function loads the specified module, extracts information about its 
    classes and functions including their docstrings and argument signatures,
    and returns this information as a dictionary.
    
    Parameters:
    module_path (str): The file path of the module to analyze.
    
    Returns:
    dict: A dictionary containing information about the module's classes and functions.
    """
    info = {
        "classes": {},
        "functions": {}
    }
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj):
            info["classes"][name] = {"methods": {}}
            for method_name, method_obj in inspect.getmembers(obj, predicate=inspect.isfunction):
                info["classes"][name]["methods"][method_name] = str(inspect.signature(method_obj))
        elif inspect.isfunction(obj):
            info["functions"][name] = str(inspect.signature(obj))
    return info