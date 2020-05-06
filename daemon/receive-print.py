import time

# 핸들러
def process_line(l):
  time.sleep(0.5)
  print(l)



with open('message.log') as f:
  doc = f.read()



def writer(doc, i):
  for s in doc[i:i+100]:
    with open('command.txt', 'a') as f:
      f.write(s)


for i in range(len(doc)):
  if i%100 == 0:
    writer(doc, i)
  else:
    process_line(i)


#with open('command.txt') as f:
#  while True:
#    line = f.read()
#    process_line(line)

#1. 파일 하나를 읽기 모드로 열었다.
#2. 한 줄씩 읽어서 process_line() 함수로 보내어 처리한다.
#3. 만약 마지막 줄을 읽은 후 더 읽을 내용이 없다면 0.5초 후에 재시도한다.
