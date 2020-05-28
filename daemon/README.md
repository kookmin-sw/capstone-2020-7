# 1. 데몬(daemon) 이란?
- 특정 서비스를 위해 백그라운드 상태에서 계속 실행되는 서버 프로세스이다.
- 데몬은 서버가 부팅될 때 메모리에 로딩이 되고 서버가 죽을 때까지 계속 자원을 할당 받고 있다.
- 사용자의 요청을 기다리고 있다가 요청이 발생하면 이에 적절히 대응하는 리스너 역할
- 데몬은 서버가 죽을 때까지 자원을 점유하고 있는 형태여서 많은 데몬이 실행된다면 자원 소비가 크다.

## 1-1. 데몬을 실행하는 방법은 크게 두 가지 : standalone, super daemon
- 자주 사용하는 데몬은 standalone 방식, 번번치 않은 데몬은 super daemon 방식으로 실행

### 1-1-1. standalone type daemon
- 독립적으로 수행되며 서비스 요청에 응답하기 위해 항시 메모리에 상주하는 데몬이다.
- 항상 동작하며 메모리에 상주해야 하기 때문에 서버의 메모리를 많이 소모하고 클라이언트의 요청이 들어올 때마다 처리를 위해 새로운 메모리를 소모한다는 점 등의 문제점이 있다. 따라서 클라이언트의 요청이 많지 않은 네트워크 서비스의 경우 스탠드얼론 방식은 비효율적이라 할 수 있다.

### 1-1-2. Inetd type daemon(super daemon)
- 서비스 요청이 있을 때만 메모리에 적재되므로 서버 부하를 상대적으로 줄일 수 있다는 장점이 있다.
- 단점은 응답속도가 standalone보다 느리다는 것이다.
- 따라서 빠른 응답속도가 필요하지 않을 경우에 이 모드를 사용한다.

## 1-2. Daemon process와 일반 process의 차이
- 일반 process는 실행 상태에 들어가 일련의 명령을 수행하고 명령이 끝나면 process가 소멸되는데 비해 daemon process는 일련의 명령이 끝나도 소멸되지 않고 메모리 상에 상주하면서 특정한 조건이 되면 다시 명령을 수행하는 process라고 한다.

***

# 2. Daemon 생성 단계
## 2-1. 특정 시간 주기마다 log 파일로부터 한 줄 씩 읽어 핸들러 함수를 실행하는 프로그램 작성
### 2-1-1. first_daemon.py
```
import time

# Full_data.log 를 다 읽어 doc에 저장
with open('Full_data.log') as f:
  doc = f.read()

# 0.25초에 한 번씩 doc의 한 줄을 Add_data에 적어준다.
for i in range(len(doc)):
  with open('Realtime.log', 'a') as f:
    f.write(str(i)+"\n")
    time.sleep(0.25)
```
#### 2-1-1-1. first_daemon.py 코드 설명
1. Full_data.log 파일을 연다.
2. 0.25초에 한 번씩 Full_data.log의 한 줄을 Realtime.log에 적어준다.

### 2-1-2. second_daemon.py
```
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
```
#### 2-1-2-1. second_daemon.py 코드 설명
1. Realtime.log 파일을 연다.
2. 무한루프를 통해 **마지막 read 지점부터** 1초 한 번씩 파일을 읽으며 process_line() 함수를 실행한다.
3. 만약 마지막 줄을 읽은 후 더 읽을 내용이 없다면 1초 후에 재시도한다.

### 2-1-3. Full_data.log
    전체 로그 데이터 역할

### 2-1-4. Realtime.log
    실시간 로그 데이터 역할

## 2-2. 처리흐름
```
$ python second_daemon.py&
$ python first_daemon.py&
```
1. second_daemon을 백그라운드로 실행
2. first_daemon을 백그라운드로 실행
3. Full_data.log 의 데이터가 0.25초 마다 한줄씩 Realtime.log 에 써지며
4. 1초마다 그 동안 쓰인 Realtime.log의 데이터를 출력한다.

## 2-3. Daemon process 확인 및 종료
```
ps 
kill -9 PID
```
- 실행된 프로세스 확인
- 프로세스 종료 




