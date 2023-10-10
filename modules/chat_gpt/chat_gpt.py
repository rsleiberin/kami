import openai
import config

class ChatGPT:
    def __init__(self):
        openai.api_key = config.OPENAI_API_KEY
    
    def generate_test(self, module_info):
        docstrings = module_info.get("docstrings", "")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a test generation assistant. Help the user create tests for their code based on the information provided."},
                {"role": "description", "content": docstrings}
            ]
        )
        generated_test = response['choices'][0]['message']['content']
        return generated_test

'''

'''