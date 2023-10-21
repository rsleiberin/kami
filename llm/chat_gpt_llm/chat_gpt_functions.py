# Import Section: Standard libraries, third-party libraries, application libraries
import json
from utils.utils import print_tracer, handle_error  # Assuming print_tracer and handle_error are in utils.utils

class ChatGPTAssistant:  # Extend the existing class

    def handle_function_call(self, function_name, function_args):
        """
        Handle function calls received from ChatGPT.
        """
        print_tracer("ChatGPTAssistant", "handle_function_call", "Start")
        
        try:
            # Implement safety checks
            if self.is_safe_function(function_name, function_args):
                print_tracer("ChatGPTAssistant", "handle_function_call", "Safe Function")
                
                json_string = json.dumps({
                    "function_name": function_name,
                    "arguments": function_args
                })
                
                return Run(json_string)  # Run function imported from run_function.py
            else:
                print_tracer("ChatGPTAssistant", "handle_function_call", "Unsafe Function")
                
                # Handle unsafe function calls
                return "Unsafe function call attempted."
        except Exception as e:
            print_tracer("ChatGPTAssistant", "handle_function_call", "Error", str(e))
            handle_error("CH001")  # Hypothetical error code
        finally:
            print_tracer("ChatGPTAssistant", "handle_function_call", "End")

    def is_safe_function(self, function_name, function_args):
        """
        Check if the function call is safe to execute.
        """
        print_tracer("ChatGPTAssistant", "is_safe_function", "Start")
        
        # Implement your safety checks here
        result = function_name in approved_functions_list  # This list needs to be defined

        print_tracer("ChatGPTAssistant", "is_safe_function", "End")
        
        return result
