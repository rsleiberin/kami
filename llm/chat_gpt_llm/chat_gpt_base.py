# Import Section: Sorted according to PEP8
from context_management.context_manager import ContextManager
from config import OPENAI_API_KEY
from utils.utils import print_tracer
from llm.chat_gpt_llm.chat_gpt_loop import ChatGPTAssistant as ChatGPTAssistant_Loop
from llm.chat_gpt_llm.chat_gpt_send import ChatGPTAssistant as ChatGPTAssistant_Send
from llm.chat_gpt_llm.chat_gpt_receive import ChatGPTAssistant as ChatGPTAssistant_Receive
from llm.chat_gpt_llm.chat_gpt_functions import ChatGPTAssistant as ChatGPTAssistant_Functions

# Pseudo-Code:
# 1. Extend ChatGPTAssistant from multiple other classes.
# 2. Initialize with API keys, system messages, and context manager.
# 3. Use methods from extended classes.

class ChatGPTAssistant(ChatGPTAssistant_Loop, ChatGPTAssistant_Send, ChatGPTAssistant_Receive, ChatGPTAssistant_Functions):
    """
    A class to handle the functionalities of the ChatGPT Assistant.
    """
    
    def __init__(self):
        print_tracer("ChatGPTAssistant", "__init__", "Start", "Initializing ChatGPTAssistant.")
        
        # Setting API Key and system messages
        self.api_key = OPENAI_API_KEY
        self.system_message = "You will output only function calls, please write a method and a message with each one by using 'run(<json>)'. Running 'run()' without an argument returns a list of json keys you can access."
        
        # Initializing the context manager
        self.context_manager = ContextManager()
        
        print_tracer("ChatGPTAssistant", "__init__", "End", "ChatGPTAssistant Initialized.")

# Main function to initiate the assistant and start the loop
if __name__ == "__main__":
    print_tracer("ChatGPTAssistant", "__main__", "Start", "Main Function Start.")
    
    print("Initializing ChatGPTAssistant...")
    chat_gpt_instance = ChatGPTAssistant()    
    chat_gpt_instance.loop()
    
    print_tracer("ChatGPTAssistant", "__main__", "End", "Main Function End.")
