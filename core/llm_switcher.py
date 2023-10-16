from modules.module_registry.module_registry import ModuleRegistry  # Assuming the ModuleRegistry is located in the same directory
from  utils.utils import print_tracer, handle_error, get_methods, add_error_codes

class LLMSwitcher:

    def __init__(self):
        self.module_registry = ModuleRegistry()
        self.current_module = None

    def switch_to_module(self, module_name: str) -> dict:
        if module_name not in self.module_registry.get_registered_modules():
            return {
                'status': 'error',
                'message': f"Module {module_name} not found in the ModuleRegistry."
            }
        
        self.current_module = module_name
        return {
            'status': 'success',
            'message': f"Switched to module {module_name} successfully."
        }

    def execute_current_module_method(self, method_name: str, *args, **kwargs) -> dict:
        if not self.current_module:
            return {
                'status': 'error',
                'message': "No module currently loaded."
            }
        
        result = self.module_registry.execute_module_method(self.current_module, method_name, *args, **kwargs)
        if not result:
            return {
                'status': 'error',
                'message': f"Failed to execute method {method_name} for module {self.current_module}."
            }

        return {
            'status': 'success',
            'message': f"Executed method {method_name} for module {self.current_module} successfully.",
            'data': result
        }

    def get_current_module_methods(self) -> dict:
        if not self.current_module:
            return {
                'status': 'error',
                'message': "No module currently loaded."
            }

        methods = self.module_registry.get_module_methods(self.current_module)
        return {
            'status': 'success',
            'message': f"Methods fetched for module {self.current_module}.",
            'data': methods
        }

if __name__ == "__main__":
    llm_switcher = LLMSwitcher()
    get_methods(llm_switcher)
    # Register dummy modules
llm_switcher.module_registry.register_module("DummyModule1", LLMSwitcher())
llm_switcher.module_registry.register_module("DummyModule2", LLMSwitcher())

# Switch modules
arg1 = "test_argument_1"
arg2 = "test_argument_2"

response = llm_switcher.switch_to_module("DummyModule1")
print(response)

response = llm_switcher.switch_to_module("DummyModule2")
print(response)

response = llm_switcher.execute_current_module_method("dummy_method1", arg1, arg2)
print(response)




