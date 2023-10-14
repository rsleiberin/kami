from types import FunctionType
import inspect

def get_methods(obj):
    """
    Gets all the methods available in the class and their information.
    """
    try:
        print(f"DT.3.1-Utils-get_methods: Starting to inspect {obj.__class__.__name__}")

        method_list = {}
        print(f"DT.3.1.1-Utils-get_methods: Inspecting {obj.__class__.__name__}")

        for name, data in inspect.getmembers(obj, predicate=inspect.ismethod):
            if name.startswith("__"):
                continue
            
            print(f"DT.3.1.2-Utils-get_methods: Method {name} Found")

            args = [a for a in inspect.getfullargspec(data).args if a != "self"]
            method_list[name] = {"args": args, "doc": str(data.__doc__).strip()}

        print(f"DT.3.1.3-Utils-get_methods: Method List Compiled")

        return method_list
    except Exception as e:
        print(f"DT.3.1-Error: Utils-get_methods: An error occurred: {str(e)}")
        return None




