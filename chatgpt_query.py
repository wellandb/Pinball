import openai
openai.api_key = "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"


models = openai.Model.list()
print(model['id'] for model in models['data'])

def main(question):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = [{"role": "user", "content": question}],
        max_tokens = 1024,
        temperature = 0.2)
    print(completion)
    print('Chat gpt fractal')

    message = completion.choices[0].message.content
    print(message)