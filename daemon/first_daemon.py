import time

# Full_data.log 를 다 읽어 doc에 저장
with open('Full_data.log') as f:
  doc = f.read()

# 0.25초에 한 번씩 doc의 한 줄을 Add_data에 적어준다.
for i in range(len(doc)):
  with open('Realtime.log', 'a') as f:
    f.write(str(i)+"\n")
    time.sleep(0.25)

