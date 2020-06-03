- D1_destinationIP (vertical Bar)
Metircs > Y_axis : count
Buckets > X-axis > Agrregation : Terms /Field : destinationIP.keyword / Order by : Metric:Count / Order : descending, size=7
- D1_destinationPort (pie)
Metircs > Slice size : count
Buckets > Split slices > Agrregation : Terms /Field : destinationPort.keyword / Order by : Metric:Count / Order : descending, size=5
- D1_markdown (Markdown)
### ## SEMO - Do mo!
### ### [Comprehensive analysis Dashboard]
### timestamp 데이터 트래픽 + 접속 IP,Port분포 + 접근 IP,Port분포+ Protocol 분포를 통해 트래픽이 유난히 많은 날짜를 확인하고, 날짜 필터를 설정해 그 날짜에 어떤 IP가 많이 접속했는지를 확인한다. 또한, 프로토콜을 확인해서 UDP인지 DNS 서비스와 같이 어떤 활동을 주로 하는지도 추측할수 있다. 정오탐 필드를 필터링해서 정탐 부분만 트래픽 분석 대시보드로 필터링 해주면 분석해야할 양이 훨씬 줄어들 것이다
- D1_protocol (Pie)
Metircs > Slice size : count
Buckets > Split slices > Agrregation : Terms /Field : protocol.keyword / Order by : Metric:Count / Order : descending, size=2
- D1_sourceIP (verical Bar)
Metircs > Y_axis : count
Buckets > X-axis > Agrregation : Terms /Field : sourceIP.keyword / Order by : Metric:Count / Order : descending, size=7
- D1_sourcePort (Pie)
Metircs > Slice size : count
Buckets > Split slices > Agrregation : Terms /Field : sourcePort / Order by : Metric:Count / Order : descending, size=5
- D1_timestamp (Line)
Metircs > Y_axis : count
Buckets > X-axis > Agrregation : Terms /Field : @timestamp / Order by : Metric:Count / Order : descending, size=58