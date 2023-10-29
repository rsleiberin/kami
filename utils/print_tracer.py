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