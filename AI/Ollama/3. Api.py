from ollama import Client

# localhost 11434 port로 
client = Client(host='http://localhost:11434')
response = client.chat(model='llama3', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])

print(f"{response['message']['content']}")