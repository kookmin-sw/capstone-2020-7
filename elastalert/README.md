## **[Elastalert 설치 가이드라인]**
해당 가이드라인은  ELK 스택 7.7버전을 사용하였습니다.

`$ pip install elastalert`
`$ git clone https://github.com/Yelp/elastalert.git`
`$ pip install "setuptools>=11.3"`
`$ python setup.py install`
`$ elastalert-create-index`

## **[Elastalert 실행 가이드라인]**
- 테스트용으로 정상적으로 실행되는지만 확인
`$ elastalert-test-rule example_rules/d.yaml `
- 실행
`$ elastalert --verbose --rule example_rules/d.yaml`

(d.yaml대신 실제로 실행할 rule을 선택.)

## **[Elastalert Example_rules 가이드라인]**
Rule타입
- **Any** : The any rule will match everything. Every hit that the query returns will generate an alert.
- **Blacklist** : The blacklist rule will check a certain field against a blacklist, and match if it is in the blacklist.
- **Whitelist** : Blacklist와 흡사 , this rule will compare a certain field to a whitelist, and match if the list does not contain the term.
- **Change** : This rule will monitor a certain field and match if that field changes.
- **Frequency** : This rule matches when there are at least a certain number of events in a given time frame.
- **Flatline** : This rule matches when the total number of events is under a given threshold for a time period.
- **New Term** :This rule matches when a new value appears in a field that has never been seen before
- **Cardinality** : This rule matches when a the total number of unique values for a certain field within a time frame is higher or lower than a threshold
- **Metric Aggregation** : This rule matches when the value of a metric within the calculation window is higher or lower than a threshold

#### samplerules.yaml
```es_host: elasticsearch.example.com
es_port: 14900
name: Example rule
type: frequency
index: logstash-*
num_events: 50
timeframe:
    hours: 4
filter:
- term:
    some_field: "some_value"
alert:
- "email"
- "slack"
email:
- "bbbbbbbbb@naver.com"
slack:
slack_webhook_url: "https://hooks.slack.com/services/T~~~9B1OvKw"
slack_username_override: 'wow159357'
slack_channel_override: '#elastalert'
slack_emoji_override: ':pizza:'
```

- es_host, es_port는 elasticsearch를 설치할떄의 ip,port번호를 적으면 된다.
- name 에 해당 룰 이름을 지정해준다.
- Type에 위에서 설명해준 Rule타입을 선택한다.
- time frame 해당 룰이 몇시간 이내에 실행된데이터를 기준으로 할지 정해준다.
- num event 에 특정데이터수를 지정해준다
- filter에 어떤 필드를 기준으로 삼을것인지 정해준다.
- alert에 'slack', 'email'등 알림받기 원하는것을 선택하여 적어준다.
- slack: 밑에 알람받을 슬랙주소와 유저주소, 채널,알람받을 이모티콘을 설정해준다.

## **[Elastalert Slack Webhook 설정]**
 1. 설정 - Add an app or custom integration 클릭
 2. 가입된 이메일+비밀번호 입력
 3. 슬렉웹페이지가 열리면 가운데 검색창에 incoming webhooks 선택
 4. 왼쪽 메뉴바에 Add Configuration누르기
 5. 메세지보낼 채널을 선택 (ex: #general)
 6. webhook URL복사후 Rule에 들어가 Slak: 아래부분  slack_webhook_url: 에 작성
