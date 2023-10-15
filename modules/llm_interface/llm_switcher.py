from modules.utils.error_handler import handle_error  # Make sure to import handle_error
import sys
import logging
from modules.utils.utils import get_methods
from modules.llm_interface.chat_gpt.chat_gpt import ChatGPT
from datetime import datetime

sys.path.append('/home/tank/kami')  # Use the actual path to the 'kami' directory

# Initialize logging
logging.basicConfig(filename='llm_switcher.log', level=logging.DEBUG)

class LLMSwitcher:
    def __init__(self):
        """
        Initialize the LLMSwitcher with registered modules.
        This serves as the main controller for managing different language models and modules.
        ---
        Debug Tag: DT.1-LLMSwitcher-Initialization
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.1-LLMSwitcher-Initialization | Time: {timestamp}")

        try:
            # Initialize AirtableClient
            self.AirtableClient = AirtableClient(config.AIRTABLE_PERSONAL_ACCESS_TOKEN)
            
            # Initialize modules dictionary
            self.modules = {
                "LLMSwitcher": self,
                "AirtableClient": self.AirtableClient  # Note the comma at the end
            }
            
            # Load sub-classes
            self.modules["AirtableClient.Read"] = self.modules["AirtableClient"].Read
            
            # Initialize ChatGPT with the modules
            self.modules["chat_gpt"] = ChatGPT(modules=self.modules, llm_switcher=self)

        except Exception as e:
            error_message, http_status = handle_error('LLM001')
            logging.error(f"{error_message} | HTTP Status: {http_status} | Exception: {e}")

    def get_methods(self):
        """
        Get methods and their docstrings for the LLMSwitcher class.
        This function provides an overview of the methods available in the LLMSwitcher class.
        ---
        Debug Tag: DT.2-LLMSwitcher-get_methods
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.2-LLMSwitcher-get_methods | Time: {timestamp}")

        try:
            return get_methods(self)
        except Exception as e:
            error_message, http_status = handle_error('LLM002')
            logging.error(f"{error_message} | HTTP Status: {http_status} | Exception: {e}")
            return {}


if __name__ == "__main__":
    """
    Main entry point for the LLMSwitcher application.
    This will initialize the LLMSwitcher class, retrieve the ChatGPT module, and enter a while loop for chat.
    ---
    Debug Tag: DT.10-main
    Debug Focus Log Tag: Main loop for chat
    """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"DT.10-main | Time: {timestamp}")

    # Initialize LLMSwitcher
    print(f"DT.10-Initializing LLMSwitcher | Time: {timestamp}")
    switcher = LLMSwitcher()

    #Get LLMSwitcher methods
    print (switcher.get_methods())









