# Importing necessary modules
import openai
import chat_api

# get the chat gpt api key for communication with chat gpt
openai.api_key = chat_api.API

# model of chat gpt to use
models = openai.Model.list()

# main function that queries chat gpt
def main(question):
    # create a chat gpt query 
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = [{"role": "user", "content": question}],
        max_tokens = 1024,
        temperature = 0.2)
    print('Chat gpt fractal:')

    # returns the first choice given by chat gpt
    message = completion.choices[0].message.content
    # print the message so that you can compare or fix code
    print(message)
    # split the message recieved into lines
    lines = message.splitlines()
    # set record to False as it usually starts with a message
    record = False
    # output list to store the python code
    output = []
    for i in lines:
        # start of python is usually an import so if this occurs start recording
        if i.startswith("import"):
            record = True
        # record the outputs
        if record:
            output.append(i)
        # if ``` occurs then it means there is a start or end of code usually but not always
        if i=="```":
            # if ``` was recorded then delete it from output
            if record:
                output.pop(-1)
            # set record to inverse
            record = not(record)
    
    # open a file to paste the python code into and clear it of all writing
    file = open("chat_fractal.py", "w")
    file.close()
    # append the output into the file
    file = open("chat_fractal.py", "a")
    for o in output:
        file.write(o)
        file.write('\n') # next line
    # clode the file
    file.close()
    # import the python code from the file you just recorded the output within
    import chat_fractal
    # run the python code
    chat_fractal