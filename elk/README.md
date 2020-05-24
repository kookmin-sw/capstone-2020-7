# ELK

해당 가이드라인은 ELK 스택 7.7 버전을 사용하였으며, 설치 및 사용에 관련된 내용은 버전별로 상이할 수 있습니다.

### 설치 순서

ELK Stack 설치 순서는 다음과 같습니다.

1. Elasticsearch
2. Kibana
3. Logstash (여기까지만 설치하시면 됩니다. 아래는 추가적으로 필요한 경우에 설치하세요)
4. Beats
5. APM Server
6. Elasticsearch Hadoop

이 순서대로 설치하면 각 제품이 의존하는 구성 요소가 제 위치에 있게 됩니다. <br>


### Elasticsearch

```
sudo wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.7.0-linux-x86_64.tar.gz
sudo wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.7.0-linux-x86_64.tar.gz.sha512
shasum -a 512 -c elasticsearch-7.7.0-linux-x86_64.tar.gz.sha512 
tar -xzf elasticsearch-7.7.0-linux-x86_64.tar.gz
```


refer by : https://www.elastic.co/guide/en/elasticsearch/reference/current/targz.html<br>

### Kibana

```
sudo curl -O https://artifacts.elastic.co/downloads/kibana/kibana-7.7.0-linux-x86_64.tar.gz
sudo curl https://artifacts.elastic.co/downloads/kibana/kibana-7.7.0-linux-x86_64.tar.gz.sha512 | shasum -a 512 -c - 
tar -xzf kibana-7.7.0-linux-x86_64.tar.gz
```

### Logstash

```
sudo curl -O https://artifacts.elastic.co/downloads/logstash/logstash-7.7.0.tar.gz
sudo curl https://artifacts.elastic.co/downloads/logstash/logstash-7.7.0.tar.gz.sha512 | shasum -a 512 -c -
tar -xvf logstash-7.7.0.tar.gz
```


### Configuration
Elasticsearch와 Kibana는 yml 추가 설정이 필요합니다.<br>
Elasticsearch Configuraiton : https://github.com/kookmin-sw/capstone-2020-7/tree/feature/ELK/elk/elasticsearch <br>
Kibana Configuration : https://github.com/kookmin-sw/capstone-2020-7/tree/feature/ELK/elk/kibana <br>


버전이 상이할 경우 각 제품별 설치 방법은 아래 링크 참고 <br>
https://www.elastic.co/guide/index.html <br>
