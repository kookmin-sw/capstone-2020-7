import time

# 핸들러
def process_line(l):
  time.sleep(5)
  print(l)


with open('message.log') as f:
  doc = f.read()

for i in range(len(doc)):
  with open('command.txt', 'wa') as f:
    f.write(str(i)+"\n")
    time.sleep(1)


#1. 파일 하나를 읽기 모드로 열었다.
#2. 한 줄씩 읽어서 process_line() 함수로 보내어 처리한다.
#3. 만약 마지막 줄을 읽은 후 더 읽을 내용이 없다면 0.5초 후에 재시도한다.
