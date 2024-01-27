# https://github.com/ollama/ollama-python
import ollama

# 1. 기본적인 채팅
count=1
response = ollama.chat(model='mistral', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
print(f"{count}. {response['message']['content']}")