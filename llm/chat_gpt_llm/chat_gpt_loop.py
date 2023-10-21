# Import Section
from utils.utils import print_tracer

# Extend the existing ChatGPTAssistant class
class ChatGPTAssistant:
    
    def loop(self):
        """
        Handles the main loop for the ChatGPT Assistant, managing user input and ChatGPT responses.
        """
        print_tracer("ChatGPTAssistant", "loop", "Start", "Initializing main loop")
        
        print("ChatGPT Assistant is ready to assist you!")
        
        while True:
            try:
                print_tracer("ChatGPTAssistant", "loop", "Event", "Waiting for user input")
                
                user_input = input("You: ").strip()
                
                if not user_input:
                    print("Empty input, try again.")
                    continue
                
                print_tracer("ChatGPTAssistant", "loop", "Event", "Fetching current context")
                
                context = self.context_manager.context_buffer  # Fetch current context from Project Kami
                
                chat_gpt_response = self.send_to_chat_gpt(context, user_input)
                
                if chat_gpt_response is not None:
                    print(f"Assistant: {chat_gpt_response}")
                    self.receive_from_chat_gpt(chat_gpt_response)
                else:
                    print("Failed to receive a valid response from ChatGPT.")
                
            except KeyboardInterrupt:
                print_tracer("ChatGPTAssistant", "loop", "Event", "User initiated exit")
                
                print("Exiting loop.")
                break
            except Exception as e:
                print_tracer("ChatGPTAssistant", "loop", "Error", f"An error occurred: {e}")
                
                print(f"An error occurred: {e}")
                continue

        print_tracer("ChatGPTAssistant", "loop", "End", "Exiting main loop")
