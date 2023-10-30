# File: handle_function_call.py

# Import Section: Standard libraries, third-party libraries, application libraries
import json
from utils.print_tracer import print_tracer
from utils.handle_error import handle_error

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
