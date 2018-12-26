# Grafana Documentation

## Dash Board
### 1. Time Range 설정
1. 대시보드 화면 우측 상단 time range 바를 클릭하면 time range와 refresh interval을 설정할 수 있다.  
2. time range는 커스텀 가능하며 Quick ranges 에서 선택할 수도 있다.

> **Time Range 설정**
> <img src="https://i.imgur.com/DRVunjL.png?1"/>

3. Graph 위에서 특정 영역을 드래그 하면 time range가 드래그 한 영역으로 변경되며 이 때 대시 보드 전체 time range 가 변한다.

> **드래그 하여 Time Range 선택**
>   
> - 영역 선택  
> <img src="https://i.imgur.com/doyN7Hn.png?1"/>  
>  
> - 결과  
> <img src="https://i.imgur.com/omH5EVQ.png?1"/>


### 2. Graph
1. 그래프 위에 마우스를 올리면 해당 시점의 수치를 확인할 수 있다.
2. 그래프 상단 제목 바를 클릭하면 그래프 관련 기능을 확인할 수 있다.
3. 그래프에 설정한 alert이나 threshold 값에 따른 상태를 그래프 제목 앞의 하트 모양의 색깔로 확인 할 수 있다. (하트 모양이 없는 그래프는 alert 설정이 없는 그래프이다.)

> **Graph 관련 기능**
> <img src="https://i.imgur.com/w9JYQdy.png?1"/>

4. 그래프의 특정 범주를 클릭하면 해당 범주의 데이터만 그래프에 그려지며 Y 축의 범위도 해당 범주 데이터에 맞게 변하여 상세하게 확인 할 수 있다.

> **특정 범주 그래프**
> <img src="https://i.imgur.com/qWCOmJ5.png?1"/>

5. alert을 설정한 그래프는 alert 상황이 발생하면 그래프 제목 앞 하트의 색이 빨간색으로 바뀌며, 그래프 주변이 붉게 깜빡거린다.
6. Zabbix 데이터 소스 플러그인은 alert 기능을 지원하지 않아 thresholds를 설정하여 대체하였다.  
  *e.g., Win Free Disk, DB Free Disk*

> **그래프 Alert**  
> <img src="https://i.imgur.com/IFgSw50.png"/>

----------------------------------------
#### *아래부터는 각 그래프에 대한 설명입니다*

### 3. Win Free Disk
1. 라이센스 서버의 여유 디스크 공간을 백분율 값으로 나타낸 그래프이다.
2. 그래프 오른쪽에 있는 테이블은 각 서버의 현재 여유 디스크 공간의 백분율 값을 표시한다.

> **Win Free Disk**
> <img src="https://i.imgur.com/6y8DeMJ.png"/>

3. Thresholds를 20으로 지정하여 서버의 Disk 여유 공간이 20% 이하가 되면 그래프 제목 앞 하트 색이 빨간색으로 바뀌며 상태 변화를 알린다.


### 4. DB Free Disk
1. 라이센스 DB 서버의 여유 DB 공간을 백분율 값으로 나타낸 그래프이다.
2. 그래프 아래쪽에 있는 테이블은 각 DB의 현재 여유 공간의 백분율 값을 표시한다.

> **DB Free Disk**
> <img src="https://i.imgur.com/jje99OB.png"/>

3. Thresholds를 20으로 지정하여 DB의 여유 공간이 20% 이하가 되면 그래프 제목 앞 하트 색이 빨간색으로 바뀌며 상태 변화를 알린다.


### 5. V1 DB Disk Usage
1. AWS Version 1 Redshift 사용량을 백분율 값으로 나타낸 그래프이다.
2. 그래프 아래쪽에 있는 테이블은 Redshift의 평균 사용량 백분율 값을 표시한다.

> **V1 DB Disk Usage**  
> <img src="https://i.imgur.com/HMPC0L6.png"/>

3. Alert을 지정하여 Redshift 사용량이 80% 이상이 되면 grafana alert system과 연동한 notification channel로 alert message가 전송되며 그래프 앞 하트 색이 빨간색으로 바뀌고, 그래프에 alert 이 발생한 시점을 표시한다.


### 6. ELB Status 200
1. AWS ELB Status 200 개수를 나타낸 그래프이다.
2. 그래프는 1분동안 ELB Status 200 Code의 합을 그린다.
3. 그래프 왼쪽에 있는 테이블은 각 ELB Status 200의 평균 값을 표시한다.

> **ELB Status 200**
> <img src="https://i.imgur.com/ZWZlJR9.png"/>


### 7. ELB Status Error 500
1. AWS ELB Status 500 개수를 나타낸 그래프이다.
2. 그래프는 1분동안 ELB Status 500 Error Code의 합을 그린다.
3. 그래프 왼쪽에 있는 테이블은 각 ELB Status 500의 평균 값을 표시한다.

> **ELB Status Error 500**
> <img src="https://i.imgur.com/C4nA2rI.png"/>

4. Alert을 지정하여 ELB Status 500 Error가 50개 이상이 되면 grafana alert system과 연동한 notification channel로 alert message가 전송되며 그래프 앞 하트 색이 빨간색으로 바뀌고, 그래프에 alert 이 발생한 시점을 표시한다.

### 8. ELB Status Error 400
1. AWS ELB Status 400 개수를 나타낸 그래프이다.
2. 그래프는 1분동안의 ELB Status 400 Error Code의 합을 그린다.
3. 그래프 왼쪽에 있는 테이블은 각 ELB Status 400의 평균 값을 표시한다.

> **ELB Status Error 400**
> <img src="https://i.imgur.com/Vlgwl9q.png"/>


### 9. Instance CPU Usage
1. AWS EC2 서버의 CPU 평균 사용량을 나타낸 그래프이다.
2. 그래프 왼쪽에 있는 테이블은 각 EC2 서버의 CPU 사용량 평균 값을 표시한다.

> **Instance CPU Usage**
> <img src="https://i.imgur.com/QCilU90.png"/>

3. Alert을 지정하여 Instance CPU Usage가 50% 이상이 되면 grafana alert system과 연동한 notification channel로 alert message가 전송되며 그래프 앞 하트 색이 빨간색으로 바뀌고, 그래프에 alert 이 발생한 시점을 표시한다.

### 10. HBO EU Network IN/OUT
1. AWS EC2 EU 서버의 Network In, Network Out을 나타낸 그래프이다.
2. 그래프는 5분동안의 Network In, Out 각각의 합을 그린다.
3. 그래프 왼쪽에 있는 테이블은 각 서버의 현재 Network In 수치를 표시한다.

> **HBO EU Network IN/OUT**
> <img src="https://i.imgur.com/qidlFPq.png"/>


### 11. Tokyo Proxy Network IN/OUT
1. AWS EC2 JP Proxy 서버의 Network In, Network Out 각각의 Sum을 나타낸 그래프이다.
2. 그래프는 5분동안의 Network In, Out 각각의 합을 그린다.
3. 그래프 왼쪽에 있는 테이블은 현재 Network In/Out 수치를 표시한다.

> **Tokyo Proxy Network IN/OUT**
> <img src="https://i.imgur.com/Rga0MyH.png"/>


### 12. ELB-Network
1. AWS ELB Network Request Count 를 나타낸 그래프이다.
2. 그래프는 1분동안의 각 ELB Network Request Count의 합을 그린다.
3. 그래프 왼쪽에 있는 테이블은 각 ELB Network Request 값의 평균 값을 표시한다.

> **ELB-Network**
> <img src="https://i.imgur.com/dw5HoIK.png"/>
