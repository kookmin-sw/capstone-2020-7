import time

# 핸들러
def process_line(l):
  print(l)

# 1초에 한번씩 Realtime.log 파일 끝까지 읽는다.
# Realtime.log에 0.25초에 한 줄씩 적히기 때문에 1초에 4줄이 출력된다.
with open('Realtime.log') as f:
  while True:
    line = f.readline()
    if not line:
      time.sleep(1)
      continue
    process_line(line)