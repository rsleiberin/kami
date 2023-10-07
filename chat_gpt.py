import openai
import config

#Setting Up Your API Key
openai.api_key = config.OPENAI_API_KEY

#Defining a Function to Chat with GPT-3
def chat_with_gpt(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
    )
    answer = response['choices'][0]['message']['content']
    return answer

#Testing the Function
if __name__ == "__main__":
    question = "Who won the world series in 2020?"
    answer = chat_with_gpt(question)
    print(answer)
