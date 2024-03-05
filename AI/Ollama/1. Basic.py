# https://github.com/ollama/o1. llama-python
import ollama

# 기본적인 채팅 [출력이 완성되면 print]
response = ollama.chat(model='llama3', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
print(f"{response['message']['content']}")