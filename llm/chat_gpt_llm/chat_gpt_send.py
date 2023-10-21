# Import Section: Standard libraries, third-party libraries, application libraries
import openai
import json
from config import OPENAI_API_KEY
from utils.utils import print_tracer

class ChatGPTAssistant:  # Extend the existing class
    
    def send_to_chat_gpt(self, context, user_message):
        """
        Sends a user message to ChatGPT and receives a response.
        
        Args:
        - context: The context in which the chat is happening.
        - user_message: The message from the user.
        
        Returns:
        - A string containing the response from ChatGPT, or None if an error occurs.
        """
        print_tracer("ChatGPTAssistant", "send_to_chat_gpt", "Start")
        
        # Set OpenAI API key
        openai.api_key = self.api_key

        # Prepare the messages and functions to send to ChatGPT
        messages = [
            {"role": "system", "content": self.system_message},
            {"role": "user", "content": user_message},
        ]
        
        functions = [
            {
                "name": "Run",
                "description": "Input a JSON file with various keys to update your context, loop a function, and message the user at the same time.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "function_name": {"type": "string"},
                        "arguments": {"type": "object"},
                    },
                    "required": ["function_name"],
                },
            }
        ]
        
        try:
            print_tracer("ChatGPTAssistant", "send_to_chat_gpt", "API Call Initiated")
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                functions=functions,
                function_call="auto",
            )
            
            response_content = completion.choices[0].message.get('content')
            function_call = completion.choices[0].message.get('function_call')
            
            print_tracer("ChatGPTAssistant", "send_to_chat_gpt", "API Call Completed")
            
            if response_content is not None:
                return response_content
            elif function_call is not None:
                return json.dumps(function_call)
            else:
                return None
        except Exception as e:
            print_tracer("ChatGPTAssistant", "send_to_chat_gpt", "Error", f"An error occurred: {e}")
            return None
        finally:
            print_tracer("ChatGPTAssistant", "send_to_chat_gpt", "End")
