class ContextManager:
    def __init__(self):
        self.current_context = {}
        self.interaction_history = InteractionHistory()   # From interaction_history.py

    def update_context(self, new_context):
        # Merge new_context with current_context
        # ...

    def validate_response(self, response):
        # Validate the response based on interaction history and current context
        # ...

    def get_context_for_chatgpt(self):
        # Prepare context for sending to ChatGPT
        # ...