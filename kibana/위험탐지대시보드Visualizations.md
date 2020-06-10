- D2_DirectionType(inbound/outbound) (Metric)
Metircs > metric : count
Buckets > Split group > Agrregation : Terms /Field : directionType.keyword / Order by : Metric:Count / Order : descending, size=2
- D2_analyResult (Area)
Metircs > Y_axis : count
Buckets > X-axis > Agrregation : Terms /Field : analyResult.keyword/ Order by : Metric:Count / Order : ascending, size=8
- D2_destinatinPort (Vertical Bar)
Metircs > Y_axis : count
Buckets > X-axis > Agrregation : Terms /Field : analyResult.keyword/ Order by : Metric:Count / Order : descending, size=5
- D2_destinationIp (Vertical Bar)
Metircs > Y_axis : count
Buckets > X-axis > Agrregation : Terms /Field : destinationIP.keyword / Order by : Metric:Count / Order : descending, size=5
- D2_markdown (Markdown)
### ## SEMO - Do Mo!
### ### [Risk Detection Dashboard]
### 위협탐지 대시보드를 활용하여 트래픽분석 대시보드에서 분석한 결과를 가지고 보다 세부적으로 분석할 수 있다. 앞서 특정 IP의 행동이 수상한 경우, 그 IP를 필터로 해서 어떤 공격이 이루어졌는지 자세히 한 눈에 분석할 수 있는 시각화 대시보드를 제공했다. 특정 IP의 공격탐지 대시보드에서 목적지 IP, 포트 번호, 총 이벤트 발생 수, 탐지 장비, 정오탐 필드, 인바운드/아웃바운드 유무 필드들을 포함하여 해당 IP의 행동이 수상한 경우 필터링하여 어떤 특정한 IP나 포트번호에 과한 시도가 있었는지, 이벤트 수가 지나치게 많은지, 정오탐 필드로 수상한 시도를 많이 하였는지를 추측할 수 있다. 이처럼 특정 공격 별로 분석이 용이할 수 있도록 실제 보안관제 대시보드들과 정보보안 공격유형들을 참고하여 대시보드를 구성하였다.
- D2_ordIDX (Metric)
Metircs > metric: count
Buckets > split group > Agrregation : Terms /Field : orgIDX.keyword / Order by : Metric:Count / Order : descending, size=5
- D2_sourcePort (Tag Cloud)
Metircs > Tag size : count
Buckets > Tags > Agrregation : Terms /Field : sourcePort / Order by : Metric:Count / Order : descending, size=5
- D2_timestamp (vertical Bar)
Metircs > metric : count
Buckets > Split rows > Agrregation : Date Histogram /Field : @timestamp / Minimum interval : Weekly