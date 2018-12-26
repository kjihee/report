# Grafana - AWS

### Data Source
- Type: **CloudWatch**
- CloudWatch details
  * Auth Provider: **Access & secret key** (Access key ID & Secret access key 는 AWS에서 부여 받은 Key 정보 입력)
  * Default Region: 모니터링 할 Instance가 있는 Region으로 선택 (Dash Board 그릴 때 다른 Region 선택 가능)
- `Save & Test` 버튼 누른 후 **Data source is working** 이라는 문구가 뜨면 연동 성공

- <img src="https://i.imgur.com/nODsguQ.png?2"/>

### Grafana - AWS Dash Board
- Panel
  * Graph, Singlestat, Table, Heatmap, Alert List 등
  * 각 패널 편집 모드에서 Axes, Legend, Display, Alert, Time Range 설정 가능
- Row 패널을 활용하여 Dash Board 내에 카테고리 생성 및 접기 가능
- Table, SingleStat 패널에서 thresholds 와 색상 설정
  > Grafana "Alert 기능 추후 버전에 추가 예정"

- Alert list
- PlugIn
  * Clock 패널을 이용하여 시계와 CountDown 가능
  * Pie Chart로 Ratio 표현 가능

- Graph panel에서 여러 Data Source, 여러 지표 혼합 가능

  > **e.g.1.**  
  > 하나의 LoadBalance에 대한 모든 지표(HTTPcode_Target_2XX, 3XX, 4XX, 5XX 등)를 하나의 graph에 표시 가능
  > <img src="https://i.imgur.com/y23Hs0g.png"/>

  > **e.g.2.**  
  > 서로 다른 계정과 다른 region에 있는 같은 OS의 NetworkIn 정보 모두를 한 graph에 표시 가능
  > <img src="https://i.imgur.com/XDkmCOy.png"/>

- Playlist를 통해 기존에 있던 여러 Dash Board를 묶어서 한번에 모니터링 가능 - 설정한 time interval 대로 자동 넘김
- Alerting - Notification
  * e-mail
  <img src="https://i.imgur.com/A6Urygk.png"/>  

  * LINE Alert
  <img src="https://i.imgur.com/lG0Tbsl.png"/>



### 그 외 Dash Board 지원 기능
- Dash Board에 생성할 수 있는 Graph 개수 제한 없음 (Loading 및 Dash Board 설정을 바꿀 시 적용 시간이 김)
- Data Source에 대한 계정 정보만 입력하면 해당 계정으로 수집하는 데이터 모두 열람 및 사용 가능
- Snapshot 기능을 제공하여 Dash Board 백업 지원
- Dash Board Settings
  * Dash Board refresh time custom → 0.5초까지 확인
  * Monitoring time range custom → 1초까지 가능
  * Versions - Dash Board 저장 시점을 기록하여 버전 관리
  * Permissions - 사용자들에게 Admin, Editor, Viewer 역할을 부여하여 Dash Board 접근 권한 관리
  * JSON Model - 해당 Dash Board의 settings 관련 데이터는 json 형태로 제공

#### CloudWatch
- Data Source Type에 맞게 Metric 지표 자동 쿼리
  * region, namespace, metric, Demensions 순


### 제한 사항
- 지표 list를 따로 보여주는 기능 없음
- Alert을 설정하기 위해 graph를 생성 해야함
