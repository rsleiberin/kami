import json

# Function registry to hold available functions
run_function_registry = {
    "assistant": lambda message: f"Assistant says: {message}",
    "get_method": lambda class_name: f"Methods for {class_name}: [Method1, Method2]"
    # Add more functions here
}

def Run(json_string):
    try:
        # Parse the JSON string to get function name and arguments
        data = json.loads(json_string)
        function_name = data.get("function_name")
        args = data.get("arguments", {})

        # Get the function from the registry
        function_to_call = run_function_registry.get(function_name)

        # Check if the function exists
        if not function_to_call:
            return json.dumps({"error": f"No function named {function_name} found."})

        # Call the function and return the output
        output = function_to_call(**args)
        return json.dumps({"output": output})

    except json.JSONDecodeError:
        return json.dumps({"error": "Invalid JSON format"})
    except Exception as e:
        return json.dumps({"error": f"An error occurred: {e}"})
