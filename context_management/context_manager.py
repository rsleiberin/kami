from context_management.sockets.feedback_socket import FeedbackSocket
from context_management.sockets.user_input_analysis_socket import UserInputAnalysisSocket  # Add this import if not already present
from context_management.sockets.requirement_mapping_socket import RequirementMappingSocket  # Add this import if not already present
from context_management.sub_agent_registry import SubAgentRegistry  # Add this import if not already present
from utils.utils import print_tracer


class ContextManager:

    def __init__(self):
        print_tracer("ContextManager", "__init__", "Start")
        # Initialization of core and auxiliary sockets.
        self.active_sockets = {}
        # Buffer to store context data.
        self.context_buffer = []
        # Default token limit.
        self.token_limit = 4096
        print_tracer("ContextManager", "__init__", "Event", "Initialized default settings")
        # Load user preferences and past interactions.
        self.load_user_data()
        # Initialize SubAgentRegistry instance
        self.sub_agent_registry = SubAgentRegistry()
        print_tracer("ContextManager", "__init__", "End")
        # TODO: update context_buffer (if this was your intent)


    def load_user_data(self):
        """Load user preferences and past interactions."""
        print_tracer("ContextManager", "load_user_data", "Start")
        # TODO: Fetch data from storage and update context_buffer.
        print_tracer("ContextManager", "load_user_data", "Event", "Fetching data (placeholder)")
        print_tracer("ContextManager", "load_user_data", "End")
    
    def add_socket(self, socket_name, socket_instance):
        """Add a new socket instance to active_sockets."""
        print_tracer("ContextManager", "add_socket", "Start")
        self.active_sockets[socket_name] = socket_instance
        print_tracer("ContextManager", "add_socket", "Event", f"Socket {socket_name} added.")
        print_tracer("ContextManager", "add_socket", "End")

    def process_socket(self, socket_name, *args, **kwargs):
        """Process a specific socket and retrieve its context."""
        print_tracer("ContextManager", "process_socket", "Start")
        print("Debug: Active Sockets:", self.active_sockets)  # Debug line
        socket_instance = self.active_sockets.get(socket_name)
        print("Debug: Socket Instance:", socket_instance)  # Debug line
        if socket_instance:
            context_data = socket_instance.process(*args, **kwargs)
            print("Debug: Context Data to be Appended:", context_data)  # Debug line
            self.context_buffer.append(context_data)
            self.manage_token_limit()
            print_tracer("ContextManager", "process_socket", "Event", f"Processed socket {socket_name}.")
        else:
            print_tracer("ContextManager", "process_socket", "Event", f"Socket {socket_name} not found.")
        print_tracer("ContextManager", "process_socket", "End")


    def manage_token_limit(self):
        """Manage context to fit within the token limit."""
        print_tracer("ContextManager", "manage_token_limit", "Start")
        
        # TODO: Implement truncation or prioritization when token limit is exceeded.
        print_tracer("ContextManager", "manage_token_limit", "Event", "Token management logic to be implemented.")
        
        print_tracer("ContextManager", "manage_token_limit", "End")

    def get_context(self):
        """Retrieve the current context buffer."""
        print_tracer("ContextManager", "get_context", "Start")
        
        context = self.context_buffer  # Retrieving context buffer
        print_tracer("ContextManager", "get_context", "Event", f"Context buffer retrieved. Size: {len(context)}")
        
        print_tracer("ContextManager", "get_context", "End")
        return context

    def activate_socket(self, socket_name, socket_instance):
        print("Debug: Inside activate_socket")  # Debug statement
        print_tracer("ContextManager", "activate_socket", "Start", f"Activating socket: {socket_name}")
        self.active_sockets[socket_name] = socket_instance
        print_tracer("ContextManager", "activate_socket", "Event", f"Socket {socket_name} activated.")
        print_tracer("ContextManager", "activate_socket", "End")


    def deactivate_socket(self, socket_name):
        """Deactivate (or remove) a specific socket, stopping its context processing."""
        print_tracer("ContextManager", "deactivate_socket", "Start", f"Deactivating socket: {socket_name}")
        
        try:
            del self.active_sockets[socket_name]
            print_tracer("ContextManager", "deactivate_socket", "Event", f"Socket {socket_name} deactivated.")
        except KeyError:
            print_tracer("ContextManager", "deactivate_socket", "Error", f"Socket {socket_name} not found.")
        
        print_tracer("ContextManager", "deactivate_socket", "End")


    def get_context_for_LLMSwitcher(self):
        """Prepare and return the context tailored for the LLM switcher."""
        print_tracer("ContextManager", "get_context_for_LLMSwitcher", "Start")
        
        try:
            context = self.context_buffer
            print_tracer("ContextManager", "get_context_for_LLMSwitcher", "Event", f"Context prepared for LLM switcher.")
        except Exception as e:
            print_tracer("ContextManager", "get_context_for_LLMSwitcher", "Error", f"An error occurred: {str(e)}")
            context = None
        
        print_tracer("ContextManager", "get_context_for_LLMSwitcher", "End")
        return context


    def clear_context(self):
        """Clear the context buffer."""
        print_tracer("ContextManager", "clear_context", "Start")
        
        try:
            self.context_buffer.clear()
            print_tracer("ContextManager", "clear_context", "Event", "Context buffer cleared.")
        except Exception as e:
            print_tracer("ContextManager", "clear_context", "Error", f"An error occurred: {str(e)}")
        
        print_tracer("ContextManager", "clear_context", "End")


    def update_token_limit(self, new_limit):
        """Update the token limit."""
        print_tracer("ContextManager", "update_token_limit", "Start", f"New limit: {new_limit}")
        
        try:
            self.token_limit = new_limit
            print_tracer("ContextManager", "update_token_limit", "Event", f"Token limit updated to {new_limit}.")
        except Exception as e:
            print_tracer("ContextManager", "update_token_limit", "Error", f"An error occurred: {str(e)}")
        
        print_tracer("ContextManager", "update_token_limit", "End")


    def save_context(self):
        """Persistently save the current context."""
        print_tracer("ContextManager", "save_context", "Start")
        
        try:
            # TODO: Implement saving logic.
            print_tracer("ContextManager", "save_context", "Event", "Context saved successfully.")
        except Exception as e:
            print_tracer("ContextManager", "save_context", "Error", f"An error occurred: {str(e)}")
        
        print_tracer("ContextManager", "save_context", "End")


    # ... Additional methods for further context processing and management ...
    def collect_feedback(self):
        """Collect feedback data from FeedbackSocket."""
        print_tracer("ContextManager", "collect_feedback", "Start")
        
        try:
            feedback_data = FeedbackSocket.collect_initial_feedback()
            self.context_buffer.append({"Feedback": feedback_data})
            print_tracer("ContextManager", "collect_feedback", "Event", "Feedback collected successfully.")
        except Exception as e:
            print_tracer("ContextManager", "collect_feedback", "Error", f"An error occurred: {str(e)}")
        
        print_tracer("ContextManager", "collect_feedback", "End")

    def check_feedback_for_issues(self):
        """Retrieve the latest feedback data from context_buffer and check for issues."""
        print_tracer("ContextManager", "check_feedback_for_issues", "Start")
        
        try:
            feedback_data = self.context_buffer[-1].get("Feedback", {})
            if FeedbackSocket.indicates_issues_or_improvements(feedback_data):
                print_tracer("ContextManager", "check_feedback_for_issues", "Event", "Issues or improvements detected.")
                # Handle issues or improvements here
            else:
                print_tracer("ContextManager", "check_feedback_for_issues", "Event", "No issues or improvements detected.")
        except Exception as e:
            print_tracer("ContextManager", "check_feedback_for_issues", "Error", f"An error occurred: {str(e)}")
        
        print_tracer("ContextManager", "check_feedback_for_issues", "End")

    
    def capture_and_analyze_user_input(self):
        print_tracer("ContextManager", "capture_and_analyze_user_input", "Start")
        try:
            input_socket = UserInputAnalysisSocket()
            user_input = input_socket.capture_user_input()
            intent = input_socket.analyze(user_input)
            self.context_buffer.append({"UserInput": user_input, "Intent": intent})
            print_tracer("ContextManager", "capture_and_analyze_user_input", "End")
        except Exception as e:
            print_tracer("ContextManager", "capture_and_analyze_user_input", "Error", f"An error occurred: {str(e)}")

    def map_requirements_based_on_intent(self, intent):
        print_tracer("ContextManager", "map_requirements_based_on_intent", "Start")
        try:
            mapping_socket = RequirementMappingSocket()
            requirements = mapping_socket.map(intent)
            self.context_buffer.append({"Intent": intent, "Requirements": requirements})
            print_tracer("ContextManager", "map_requirements_based_on_intent", "End")
        except Exception as e:
            print_tracer("ContextManager", "map_requirements_based_on_intent", "Error", f"An error occurred: {str(e)}")

    def register_agent(self, agent):
        print_tracer("ContextManager", "register_agent", "Start")
        try:
            self.sub_agent_registry.register(agent, "agent")
            self.context_buffer.append({"Action": "Registered", "Agent": agent})
            print_tracer("ContextManager", "register_agent", "End")
        except Exception as e:
            print_tracer("ContextManager", "register_agent", "Error", f"An error occurred: {str(e)}")

    def register_sub_agent(self, sub_agent):
        print_tracer("ContextManager", "register_sub_agent", "Start")
        try:
            self.sub_agent_registry.register(sub_agent, "sub_agent")
            self.context_buffer.append({"Action": "Registered", "SubAgent": sub_agent})
            print_tracer("ContextManager", "register_sub_agent", "Event", f"Sub-agent registered: {self.sub_agent_registry.get_active_agents()}")
            print_tracer("ContextManager", "register_sub_agent", "End")
        except Exception as e:
            print_tracer("ContextManager", "register_sub_agent", "Error", f"An error occurred: {str(e)}")

    def get_active_sub_agents(self):
        print_tracer("ContextManager", "get_active_sub_agents", "Start")
        try:
            active_sub_agents = self.sub_agent_registry.get_active_agents("sub_agent")
            self.context_buffer.append({"Action": "Fetched", "ActiveSubAgents": active_sub_agents})
            print_tracer("ContextManager", "get_active_sub_agents", "End")
        except Exception as e:
            print_tracer("ContextManager", "get_active_sub_agents", "Error", f"An error occurred: {str(e)}")
