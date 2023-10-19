# 1. Import Section
from safety.permission_management import load_whitelist, load_user_permissions  # application libraries
from safety.function_execution import execute_function  # application libraries
from utils.utils import print_tracer, handle_error  # application libraries

# Class: HumanInTheLoop
class HumanInTheLoop:
    """
    A class to manage the execution of functions with human-in-the-loop checks.
    """

    # 2.1 __init__
    def __init__(self):
        print_tracer("HumanInTheLoop", "__init__", "Start")
        # Load global settings
        self.whitelist = load_whitelist()
        self.user_permissions = load_user_permissions()
        print_tracer("HumanInTheLoop", "__init__", "End")

    # 2.2 execute_function_with_hitl
    def execute_function_with_hitl(self, func_call, user_id):
        """
        Execute a given function after performing human-in-the-loop checks.
        """
        print_tracer("HumanInTheLoop", "execute_function_with_hitl", "Start")
        try:
            # Whitelist Layer
            if func_call in self.whitelist:
                return execute_function(func_call, user_id)
            # User-Specific Permissions Layer
            if func_call in self.user_permissions.get(user_id, []):
                return execute_function(func_call, user_id)
            # Human-in-the-Loop Layer
            if not self.human_approval(func_call, user_id):
                return "Command not approved"
            # Execute the function if all checks pass
            return execute_function(func_call, user_id)
        except Exception as e:
            print_tracer("HumanInTheLoop", "execute_function_with_hitl", "Error")
            handle_error(e)
        print_tracer("HumanInTheLoop", "execute_function_with_hitl", "End")

    # 2.3 human_approval
    def human_approval(self, func_call, user_id):
        """
        Obtain human approval for executing a given function.
        """
        print_tracer("HumanInTheLoop", "human_approval", "Start")
        approval = input(f"User {user_id} is trying to execute {func_call}. Approve? (y/n): ")
        print_tracer("HumanInTheLoop", "human_approval", "End")
        return approval.lower() == 'y'
