import openai
import chat_api

openai.api_key = chat_api.API


models = openai.Model.list()

def main(question):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = [{"role": "user", "content": question}],
        max_tokens = 1024,
        temperature = 0.2)
    print('Chat gpt fractal:')

    message = completion.choices[0].message.content
    print(message)