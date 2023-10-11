import sys
from modules.utils.utils import get_methods
import config

sys.path.append('/home/tank/kami')  # Use the actual path to the 'kami' directory
from modules.llm_interface.chat_gpt.chat_gpt import ChatGPT
from modules.databases.airtable_client.airtable_client import AirtableClient

class LLMSwitcher:
    """
    A class for managing different language models (LLMs) and modules.
    """
    def __init__(self):
        """Initialize the LLMSwitcher with registered modules."""
        self.gpt = ChatGPT()
        self.airtable_client = AirtableClient(config.AIRTABLE_PERSONAL_ACCESS_TOKEN)
        
        self.modules = {
            "chat_gpt": self.gpt,
            "airtable_client": self.airtable_client
        }

    def get_methods(self):
        """Get methods for the LLMSwitcher class."""
        return get_methods(self)

    def register_module(self, module_name, module_instance):
        """Register a module with the LLMSwitcher."""
        self.modules[module_name] = module_instance

    def execute_module_method(self, module_name, method_name, *args, **kwargs):
        """Execute a specific method from a registered module."""
        module = self.modules.get(module_name)
        if not module:
            return f"No module named {module_name} found."
        
        method_to_call = getattr(module, method_name, None)
        if not method_to_call:
            return f"Method {method_name} not found in module {module_name}."

        try:
            return method_to_call(*args, **kwargs)
        except Exception as e:
            return str(e)

    def get_registered_module_methods(self, module_name):
        """Return the methods of a registered module."""
        module = self.modules.get(module_name)
        if not module:
            return f"No module named {module_name} found."
        return get_methods(module)

    def get_model_for_task(self, task_name):
        """Determine the best LLM for a given task."""
        if task_name in ["chat", "generate_text"]:
            return self.gpt
        return None

    def perform_task(self, task_name, *args, **kwargs):
        """Perform a task using the best-suited LLM."""
        model = self.get_model_for_task(task_name)
        if model:
            return model.perform(task_name, *args, **kwargs)
        return "No suitable model found for the task."
    def use_module(self, module_name, method_name, *args, **kwargs):
        """
        Use a specific method from a registered module.

        Args:
            module_name (str): The name of the module.
            method_name (str): The name of the method in the module to call.
            *args: Positional arguments to pass to the method.
            **kwargs: Keyword arguments to pass to the method.

        Returns:
            Any: The result of the method call or an error message.
        """
        module_instance = self.modules.get(module_name)
        if not module_instance:
            return f"Module {module_name} not registered."

        try:
            method = getattr(module_instance, method_name)
            return method(*args, **kwargs)
        except AttributeError:
            return f"Method {method_name} not found in module {module_name}."
        except Exception as e:
            return f"Error while using {method_name} from {module_name}: {str(e)}"

if __name__ == "__main__":
    switcher = LLMSwitcher()
    
    # Display the registered modules
    print(switcher.modules.keys())
    
    # Display the methods of LLMSwitcher
    print(switcher.get_methods())
    
    # Display the methods of AirtableClient
    print(switcher.get_registered_module_methods("airtable_client"))
    
    # Call and display the 'get_methods' of AirtableClient using 'use_module'
    result = switcher.use_module("airtable_client", "get_methods")
    print(result)


