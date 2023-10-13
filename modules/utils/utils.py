import inspect
import logging
from datetime import datetime

# Initialize the logging for error handling
logging.basicConfig(filename='utils_error.log', level=logging.ERROR)

def get_methods(obj):
    """
    Retrieve all callable methods of an object.
    ---
    Debug Tag: DT.3.1-Utils-get_methods
    """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"DT.3.1-Utils-get_methods | Time: {timestamp}")
    
    try:
        methods = {}
        
        for attr_name in dir(obj):
            # Exclude __class__ and other undesired attributes
            if attr_name in ['__class__']:
                continue
            
            attr_value = getattr(obj, attr_name)
            
            # If the attribute is a method of the object
            if callable(attr_value) and not attr_name.startswith("__"):
                methods[attr_name] = {
                    'args': list(inspect.signature(attr_value).parameters.keys()),
                    'doc': attr_value.__doc__.split('\n')[0] if attr_value.__doc__ else ''
                }
            
            # If the attribute is a class (indicating a nested class)
            elif inspect.isclass(attr_value):
                nested_methods = {}
                for nested_func in dir(attr_value):
                    nested_attr = getattr(attr_value, nested_func)
                    if callable(nested_attr) and not nested_func.startswith("__"):
                        nested_methods[nested_func] = {
                            'args': list(inspect.signature(nested_attr).parameters.keys()),
                            'doc': nested_attr.__doc__.split('\n')[0] if nested_attr.__doc__ else ''
                        }
                methods[attr_name] = {
                    'methods': nested_methods,
                    'doc': attr_value.__doc__ if attr_value.__doc__ else ''
                }

        return methods

    except Exception as e:
        logging.error(f"Error in get_methods for object {obj}: {e}")
        return {}


