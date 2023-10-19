# Import required modules and classes
from utils.utils import print_tracer
from llm.chat_gpt import ChatGPTLLM  # Assuming ChatGPTLLM is in this location

class ChatGPTInteraction:
    """
    Handles interactions with ChatGPT.
    """

    def __init__(self):
        print_tracer("ChatGPTInteraction", "__init__", "Start")
        # Initialize any required settings or variables
        self.chat_gpt_llm = ChatGPTLLM()
        print_tracer("ChatGPTInteraction", "__init__", "End")

    def send_message(self, message, context):
        print_tracer("ChatGPTInteraction", "send_message", "Start")
        # Code to send message to ChatGPT
        response = self.chat_gpt_llm.process_request(message, context)
        # Utilize print_tracer for debugging and context
        print_tracer("ChatGPTInteraction", "send_message", "Processing")
        # Extract and return the response from ChatGPT
        print_tracer("ChatGPTInteraction", "send_message", "End")
        return response  # Return the response from ChatGPT

# Error Handling
# Incorporate try-except blocks for methods that might raise exceptions
# Use print_tracer to trace errors
