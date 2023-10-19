# Import required modules
from utils.utils import print_tracer  # Import print_tracer for debugging and context

# Function to execute a given function call
def execute_function(func_call, user_id):
    print(f"[Debug] Executing function: {func_call}, User: {user_id}")
    print_tracer("function_execution", "execute_function", "Start")
    # ... (rest of the code remains the same)
    print_tracer("function_execution", "execute_function", "End")
    return "Function Executed"  # Updated this line