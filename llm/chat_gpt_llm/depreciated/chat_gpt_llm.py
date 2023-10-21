import openai
import json
from context_management.context_manager import ContextManager
from llm.chat_gpt_llm.run_funciton import Run
from config import OPENAI_API_KEY
from utils.utils import print_tracer

# Function registry to hold available functions
available_functions = {
    "Run": Run,  # Assume Run function is defined somewhere
}
'''
# Example JSON message that ChatGPT can send to query available functions
{
    "function_name": "query_available_functions",
    "arguments": {}
}
'''

class ChatGPTAssistant:
    def __init__(self):
        self.api_key = OPENAI_API_KEY
        self.system_message = "You will output only function calls, please write a method and a message with each one by using 'run(<json>)'. Running 'run()' without an arguement returns a list of json keys you can access."
        self.context_manager = ContextManager()

    def send_to_chat_gpt(self, context, user_message):
        print_tracer("ChatGPTAssistant", "send_to_chat_gpt", "Start")

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
        
        # Set OpenAI API key
        openai.api_key = self.api_key

        # Print debugging info
        print_tracer("ChatGPTAssistant", "send_to_chat_gpt", "Event", f"Messages being sent: {messages}")
        print_tracer("ChatGPTAssistant", "send_to_chat_gpt", "Event", f"Functions being sent: {functions}")

        try:
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                functions=functions,
                function_call="auto",
            )
            # ... same logging code
            response_content = completion.choices[0].message.get('content')
            function_call = completion.choices[0].message.get('function_call')
            if response_content is not None:
                return response_content
            elif function_call is not None:
                return json.dumps(function_call)
            else:
                return None
        except Exception as e:
            # Handle exceptions and print debugging info
            print_tracer("ChatGPTAssistant", "send_to_chat_gpt", "Event", f"Failed to get response: {e}")
            return None

        finally:
            print_tracer("ChatGPTAssistant", "send_to_chat_gpt", "End")

    def receive_from_chat_gpt(self, chat_gpt_response):
        print_tracer("ChatGPTAssistant", "receive_from_chat_gpt", "Start")

        if chat_gpt_response is None:
            print_tracer("ChatGPTAssistant", "receive_from_chat_gpt", "Event", "Received NoneType from ChatGPT")
            return

        print("Full object received from ChatGPT:")
        print(chat_gpt_response)
        print_tracer("ChatGPTAssistant", "receive_from_chat_gpt", "Event", f"chat_gpt_response type: {type(chat_gpt_response)}")

        try:
            # Try decoding the JSON. If it fails, it's likely a regular message.
            chat_gpt_response_dict = json.loads(chat_gpt_response)
            print_tracer("ChatGPTAssistant", "receive_from_chat_gpt", "Event", "JSON successfully decoded")

            function_call = chat_gpt_response_dict.get("function_call")
            if function_call:
                function_name = function_call.get("name")
                function_args = function_call.get("arguments")
                self.handle_function_call(function_name, function_args)  # Assuming this method exists
                print_tracer("ChatGPTAssistant", "receive_from_chat_gpt", "Event", f"Function {function_name} called with arguments {function_args}")

        except json.JSONDecodeError:
            # Handle regular messages here
            print_tracer("ChatGPTAssistant", "receive_from_chat_gpt", "Event", "Failed to decode JSON, likely a regular message")
            print("Regular message received, printing the string for inspection:")
            print(chat_gpt_response)

        print_tracer("ChatGPTAssistant", "receive_from_chat_gpt", "End")


        print_tracer("ChatGPTAssistant", "receive_from_chat_gpt", "End")
    
    def handle_function_call(self, function_name, function_args):
        # Implement safety checks, logging, etc. here
        if self.is_safe_function(function_name, function_args):
            json_string = json.dumps({
                "function_name": function_name,
                "arguments": function_args
            })
            return Run(json_string)
        else:
            # Handle unsafe function calls
            return "Unsafe function call attempted."

    def is_safe_function(self, function_name, function_args):
        # Implement your safety checks here
        return function_name in approved_functions_list


    def update_function_registry(self):
        # Update 'available_functions' based on a JSON file or a database query
        pass

    def query_available_functions(self):
        return json.dumps({"available_functions": list(available_functions.keys())})

    def loop(self):
        print_tracer("ChatGPTAssistant", "loop", "Start")
        
        print("ChatGPT Assistant is ready to assist you!")
        
        while True:
            try:
                user_input = input("You: ").strip()
                if not user_input:
                    print("Empty input, try again.")
                    continue
                
                print_tracer("ChatGPTAssistant", "loop", "Event", f"User input received: {user_input}")
                
                context = self.context_manager.context_buffer  # Fetch current context from Project Kami
                
                print("Sending to ChatGPT with context:", context)
                
                chat_gpt_response = self.send_to_chat_gpt(context, user_input)
                
                if chat_gpt_response is not None:
                    print(f"Assistant: {chat_gpt_response}")
                    print_tracer("ChatGPTAssistant", "loop", "Event", "Response sent to user")
                    self.receive_from_chat_gpt(chat_gpt_response)
                else:
                    print("Failed to receive a valid response from ChatGPT.")
                
            except KeyboardInterrupt:
                print("Exiting loop.")
                break
            except Exception as e:
                print(f"An error occurred: {e}")
                continue

        print_tracer("ChatGPTAssistant", "loop", "End")


if __name__ == "__main__":
    print_tracer("Main", "__main__", "Start")
    chat_gpt_instance = ChatGPTAssistant()
    chat_gpt_instance.loop()
    print_tracer("Main", "__main__", "End")
