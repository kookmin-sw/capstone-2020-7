### 키바나 대시보드 만드는 큰순서
1. Discover -> change index pattern에서 대시보드를 만들 index설정 ->show dates에서 적절한 date범위 조절
2. Visualization -> create visualization ->시각화하고싶은 방법선택(ex:수직바차트,파이차트) -> data index 를 선택한다> 보이고 싶은 조건에 맞추어 구성
3. Dashboard -> create dashboard -> create new버튼으로 visualization 새로 생성 or add 버튼눌러서 만들어둔 visualization들 중 선택


### Visualization 구성방법
데이터 시각화를 시작하려면 사이드 탐색 메뉴에서 시각화 를 클릭합니다.
![image](https://user-images.githubusercontent.com/50091802/83533995-3e8fa700-a52b-11ea-81bf-a80712492467.png)

시각화 툴을 사용하여 데이터를 다양한 방식으로 볼 수 있습니다.
#### Pie chart를 사용하여 데이터를 살펴보도록 하겠습니다.
시작하려면 시각화 목록에서 Pie 를 클릭합니다. 기본 검색은 모든 문서에 대해 일치 여부를 비교합니다. 처음에는 하나의 "슬라이스"가 전체 파이를 보여줍니다.
![image](https://user-images.githubusercontent.com/50091802/83534779-3be18180-a52c-11ea-8c5a-098002370d89.png)

차트에 표시할 슬라이스를 나누려면 Elasticsearch Bucket 집계를 사용합니다. 예를 들어 포트번호 분포를 파이차트로 나눠서 볼수있습니다.
각 포트번호별로 슬라이스하기 위해 다음을 수행합니다.

1. Aggregation을 선택합니다 개수로 분포를 나누기위해서는 Terms를 사용합니다.
2. 필드 목록에서 포트번호 필드를 선택합니다.
3. Order 부분에서 Metric:Count를 사용하여 Count를 선택합니다 (개수를 기준으로 삼기 때문)
4. Order에서 오름차순과 내림차순을 선택해주고 바차트에 보여줄 개수를 고릅니다. 만약 Descending : 5로 선택하면 큰수에서 작은수로 내림차순으로 5개의 프로토콜이 보여지게 됩니다.
5. 만약 뚫린 파이차트가 싫다면 OPtions - Donut부분을 선택해제 해주면 꽉찬 동그라미모양의 파이차트가 됩니다.
또 파이차트옆 내림차순으로 포트번호5개리스트 위치를 바꾸고 싶다면 Legend position - bottom으로 상하좌우 위치를 선택해주면 됩니다.

![image](https://user-images.githubusercontent.com/50091802/83536112-c8407400-a52d-11ea-8545-7d3f10928b1e.png)

![image](https://user-images.githubusercontent.com/50091802/83536367-15244a80-a52e-11ea-8424-8d1522de4adb.png)


내림차순이나 오름차순이 아니라 직접 범위를 지정한 버킷을 지정해주고싶다면,
1. 분할 슬라이스 버킷 유형을 클릭합니다.
2. 집계 목록에서 범위 를 선택합니다.
3. 필드 목록에서 해당필드를 선택합니다.
4. 범위 추가로 범위를 직접 지정해줍니다.

![image](https://user-images.githubusercontent.com/50091802/83537000-f1adcf80-a52e-11ea-8852-51c62f2daf18.png)




####  .
#### 이번엔 Vertical Bar을 사용하여 데이터를 살펴보도록 하겠습니다.
#### (Pie chart의 슬라이스 = x axis 으로 조건을 나누는부분은 동일합니다)

1. 새로 만들기 를 클릭하고 'Vertical Bar’를 선택합니다.
2. Index 패턴을 선택합니다. 아직 어떤 버킷도 정의하지 않았으므로 커다란 하나의 바가 나타나 총 문서 수를 표시합니다.
3. Metric 집계의 y-axis에서 개수가 디폴트로 지정되어 있습니다. 만약 Max, Average, Min등 갯수가아닌 기준으로 바차트를 보이고싶다면 선택해줍니다. 예시에서는 count를 선택하였습니다.
4. X축을 설정해주기위해서는 Bucket -> X-axis을 선택한다음 agrregation에서 Terms을 선택해줍니다. 파이차트와 바차트에서는 주로 갯수를 보기위해 많이쓰이므로 대부분 Terms를 사용합니다.
5. 앞서 보았던 파이차트와 동일하게 Order by, Order를 지정해줍니다.
(만약 갯수가 아니라 알파벳순으로 나열하고싶다면 order by: Alphabetical로 설정해줍니다.

![image](https://user-images.githubusercontent.com/50091802/83538557-e9ef2a80-a530-11ea-9708-661aaefd6752.png)

만약 , 바차트에서 두가지 필드를 보고싶다면 , 예를들어 목적지 포트번호를 내림차순으로 5개가 있는데 80번포트번호의 attatckType 구성을 보고싶다면
1. Buckets 에서 추가버튼클릭 -> Split series -> Terms -> AccidentType필드선택 -> order by: count-> 내림차순 으로 원하는 갯수 지정해주면 됩니다.

![image](https://user-images.githubusercontent.com/50091802/83543182-02624380-a537-11ea-8da6-773dd47c8911.png)
#### .
#### 데이터 총갯수나, 필드값에서 가장많은 값을 단편적으로 알고싶다면 gauge를 활용합니다.

생성하기를 누르면 디폴트로 해당 index의 총 데이터 갯수가 나타나게 됩니다.
![image](https://user-images.githubusercontent.com/50091802/83543579-93d1b580-a537-11ea-9c75-de968c5213c5.png)

이것은 데이터의 총 개수나 퍼센테이지를 나타내는데 주로 쓰입니다.
만약, 간단하게 어떤 필드값이 가장 많은지 단편적으로 보고싶다면
1. Metric -> aggregtaion : Max로 설정해준다음
2. 필드를 선택합니다 (attackType)
3. 옵션에서 Range를 설정해줍니다.

![image](https://user-images.githubusercontent.com/50091802/83545149-c54b8080-a539-11ea-87e1-5649259e34ef.png)

또 각 필드별로 퍼센티지를 보고싶다면
1. Metric -> aggregtaion : Max로 설정해준다음
2. 필드를 선택합니다 (attackType)
3. 옵션에서 Range를 설정해줍니다.
4. Buckets 에서 agrregtaion: Terms 선택
5. 필드는 같은것으로 선택 (attackType)
6. Order by 의 size개수를 변경하여 보여질 Guage 갯수를 지정한다.

![image](https://user-images.githubusercontent.com/50091802/83545911-dea0fc80-a53a-11ea-8a77-0eb705c1af45.png)


#### Tag Cloud는 가장 많은 필드들을 추려 보여준다.

1. Metrics : count
2. Buckets에서  Tag를 추가
3. Aggregation을 terms로 지정해준다음 필드를 선택한다.
4. 가장많은 5가지 내용을 보고싶다면 Descending : 5를 선택한다

![image](https://user-images.githubusercontent.com/50091802/83547181-cc27c280-a53c-11ea-80db-b9a69ed4b110.png)


#### Line 과 Area는 채워져있나 안채워있나의 차이로 생긴것이 매우 흡사하다. (Line 옵션- Metric -Char type 에서 area로 변경해주면 Area와 Line의 차이가 거의 없다.
#### Timestamp별로 데이터 입력 흐름을 볼때 , 전체적인 붆포도를 볼떄 주로 쓰인다.

Area에서 전체적인 분포도를 살펴보고싶다면

1. Metrics : count
2. Buckets에서 x-axis추가하기
3. Histogram선택
4. 필드선택 ( sourcePort)
5. interval을 적절히 설정해준다.
![image](https://user-images.githubusercontent.com/50091802/83548335-9388e880-a53e-11ea-9987-4a8916ed600b.png)

Line에서 Timestamp별로 발생한 이벤트의 수를 시간대별로 보고싶다면

1. Metrics : count
2. Buckets 의 x-axis 누르고 aggregation : Date Histogram선택
3. 필드는 @timestamp로 지정
4. Minimum interval은 데일리,위클리 적절한것으로 선택한다.
![image](https://user-images.githubusercontent.com/50091802/83549321-18283680-a540-11ea-8fe7-035ba28a4a3f.png)


Lined에서 실시간 음원차트처럼 만들수도 있다. 실시간 input되는 데이터중 attackType이 0,1인경우를 나누어서 보인다. (attackType은 가짓수가 적지만 가짓수가 많을경우 range말고 내림차순으로해도 괜찮다)
1. Metrics : count
2. Bucket X-axis 의 aggregation에서 Date Histogram선택
3. 필드는 @timestamp선택
4. interval은 시간별,날짜별,주별  선택해준다. 시간별로 세부적으로 보고싶다면 하루날짜를 필터링하여 시간별로 나눌수도 있다.
5. Bucket에 Split series를 추가해준다.
6. Sub aggregation : Range 설정후  필드도 설정해준다(attackType선택)
7. Range 범위정해주기.

![image](https://user-images.githubusercontent.com/50091802/83552486-d3eb6500-a544-11ea-9721-a565f73d8d1f.png)





