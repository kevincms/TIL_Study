import os
count=1

# 1. 현재 파일 경로, 실제경로, 절대경로
print("%d. %s\n   %s\n   %s"%(count,__file__,os.path.realpath(__file__),os.path.abspath(__file__))) 
count+=1

print("%d. %s"%(count,os.path.dirname(__file__))) # 2. 현재 폴더 경로
count+=1

print("%d. %s"%(count,os.getcwd())) # 3. 현재 작업 디렉토리 확인
count+=1