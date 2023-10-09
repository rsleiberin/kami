import openai
import config

#Setting Up Your API Key
openai.api_key = config.OPENAI_API_KEY

#Defining a Function to Chat with GPT-3
def chat_with_gpt(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert financial assitant. Help the user organize their finances only witholding information that is legally obligated to be obtained from a licesned professional."},
            {"role": "user", "content": question}
        ]
    )
    answer = response['choices'][0]['message']['content']
    return answer

#Testing the Function
if __name__ == "__main__":
    question = "I am creating an AI automation business and need to understand what markets are unsaturated enough to allow for entry from a junior in the field with no capital."
    answer = chat_with_gpt(question)
    print(answer)
