import time

# 핸들러
def process_line(l):
  print(l)

with open('message.log') as f:
  while True:
    line = f.readline()
    if not line:
      time.sleep(0.5)
      continue
    process_line(line)

#1. 파일 하나를 읽기 모드로 열었다.
#2. 한 줄씩 읽어서 process_line() 함수로 보내어 처리한다.
#3. 만약 마지막 줄을 읽은 후 더 읽을 내용이 없다면 0.5초 후에 재시도한다.
