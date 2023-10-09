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