import time

# 핸들러
def process_line(l):
  time.sleep(0.5)
  print(l)

with open('Full_data.log') as f:
  doc = f.read()

def writer(doc, i):
  for s in doc[i:i+100]:
    with open('Realtime.log', 'a') as f:
      f.write(s)

for i in range(len(doc)):
  if i%100 == 0:
    writer(doc, i)
  else:
    process_line(i)

