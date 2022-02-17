import time
start = time.time()

# 시간 측정 코드
test=1
for _ in range(1000000): test+=1

end = time.time()
print(end-start)