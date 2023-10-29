# Import Section: Standard libraries, third-party libraries, application libraries
import json
from utils.print_tracer import print_tracer

class ChatGPTAssistant:  # Extend the existing class
    
    def receive_from_chat_gpt(self, chat_gpt_response):
        """
        Handles the response received from ChatGPT.
        
        Args:
        - chat_gpt_response (str): The response from ChatGPT in JSON string format.
        """
        print_tracer("ChatGPTAssistant", "receive_from_chat_gpt", "Start")
        
        # Return if no response is received
        if chat_gpt_response is None:
            return

        try:
            # Parse the received JSON string
            chat_gpt_response_dict = json.loads(chat_gpt_response)
            function_call = chat_gpt_response_dict.get("function_call")
            
            # Handle function call if exists
            if function_call:
                function_name = function_call.get("name")
                function_args = function_call.get("arguments")
                
                print_tracer("ChatGPTAssistant", "receive_from_chat_gpt", "Handling Function Call")
                
                self.handle_function_call(function_name, function_args)
        except json.JSONDecodeError:
            print_tracer("ChatGPTAssistant", "receive_from_chat_gpt", "Error")
        finally:
            print_tracer("ChatGPTAssistant", "receive_from_chat_gpt", "End")
