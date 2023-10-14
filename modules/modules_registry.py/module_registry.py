class ModuleRegistry:
    def __init__(self):
        """
        Initialize the ModuleRegistry with registered modules.
        """
        try:
            # Initialize AirtableClient
            self.AirtableClient = AirtableClient(config.AIRTABLE_PERSONAL_ACCESS_TOKEN)
            
            # Initialize modules dictionary
            # Note: 'self' refers to this instance of ModuleRegistry
            # Note: 'self.AirtableClient' refers to the instance of the AirtableClient class
            self.modules = {
                "ModuleRegistry": self,  # Storing reference to this instance
                "AirtableClient": self.AirtableClient  # Storing reference to the AirtableClient instance
            }
            
        except Exception as e:
            # Error handling will be added later
            pass

    def execute_module_method(self, module_name, code, *args, **kwargs):
        """
        Execute a method from a registered module dynamically.
        This function allows you to call a method in a module by its name and pass arguments to it.
        ---
        Debug Tag: DT.4-ModuleRegistry-execute_module_method
        Debug Focus Log Tag: Executing method from module
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"DT.4-ModuleRegistry-execute_module_method | Time: {timestamp}")
        
        try:
            # Debugging information
            print(f"DT.4-Executing Module Method {module_name}.{code} | Time: {timestamp}")
            print(f"DT.4-Executed Args: {args} | Time: {timestamp}")
            print(f"DT.4-Executed Kwargs: {kwargs} | Time: {timestamp}")

            # Actual functionality
            components = code.split('.')
            module_instance = self.modules.get(module_name)  # Changed to self.module_dict

            if not module_instance:
                error_message, http_status = handle_error('MR004')  # Error codes should also be updated
                logging.error(f"{error_message} | HTTP Status: {http_status}")
                return error_message

            current_instance = module_instance
            for component in components:
                if "(" in component and ")" in component:
                    method_name, method_args_str = component.split('(')
                    method_args_str = method_args_str.rstrip(')')
                    method_args = eval(f"[{method_args_str}]")
                    current_instance = getattr(current_instance, method_name)(*method_args)
                else:
                    current_instance = getattr(current_instance, component)

            if callable(current_instance):
                print(f"DT.4-Executing function: {module_name}.{code} with args: {args} and kwargs: {kwargs} | Time: {timestamp}")
                return current_instance(*args, **kwargs)
            else:
                return current_instance

        except Exception as e:
            error_message, http_status = handle_error('MR005')  # Error codes should also be updated
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"DT.4-Exception in ModuleRegistry-execute_module_method | Time: {timestamp}")
            logging.error(f"{error_message} | HTTP Status: {http_status} | Exception: {e}")
            return str(e)