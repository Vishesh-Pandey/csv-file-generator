from ollama import chat
from ollama import ChatResponse

user_input = input("Enter input : ")

response: ChatResponse = chat(model='llama3.2:1b', messages=[
    {
        'role': 'assistant',
        'content': 'You have to only generate textual for csv file sperated by comma and new line. The output should not contain anything else.',
    },
    {
        'role': 'user',
        'content': user_input,
    },
])

# print(response)

print(response['message']['content'])

data = response['message']['content']

file = open("output.csv", "w")
file.write(data)
file.close()

# or access fields directly from the response object
print(response.message.content)