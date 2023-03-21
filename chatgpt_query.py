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
    lines = message.splitlines()
    record = False
    output = []
    for i in lines:
        if i.startswith("import"):
            record = True
        if record:
            output.append(i)
        if i=="```":
            if record:
                output.pop(-1)
            record = not(record)
        
    print(lines)
    file = open("chat_fractal.py", "w")
    file.close()
    file = open("chat_fractal.py", "a")
    for o in output:
        file.write(o)
        file.write('\n')
    file.close()
    import chat_fractal
    chat_fractal