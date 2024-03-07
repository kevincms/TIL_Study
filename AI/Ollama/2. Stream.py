import ollama

# 기본적인 채팅 [출력이 만들어지는 과정을 실시간으로 출력]
stream = ollama.chat(
    model='llama3',
    messages=[{'role': 'user', 'content': 'Why is the sky blue?'}],
    stream=True,
)

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)