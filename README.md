# [지역:상주] 특정 지역 인구 및 주간보호센터 데이터 수집/가공 프로그램
<br>

## [개발 동기]<br>
Kmong에서 개발 외주를 받아서 만들게 되었다. 의뢰인은 상주 지역 구별 70세이상 인구를 파악하고, 주간보호센터 위치 및 정원을 파악하길 바랬다.
<br><br><br>

## [개발 결과]<br>
Kmong 후기 <br><br>
![image](https://user-images.githubusercontent.com/58064919/172087231-8817f904-3563-4b7d-b69e-d4809dd46f8f.png)

<br><br><br>

## [크롤링 대상]<br><br>
NHISS / 국민건강보험자료 공유서비스
https://nhiss.nhis.or.kr/bd/ay/bdaya001iv.do
<br>
Sangju / 상주시 시청 홈페이지
https://www.sangju.go.kr/board/list.tc?mn=2404&mngNo=389&pageSeq=2564
<br><br><br>

## [개발 언어]<br><br>
Python
library: BeautifulSoup, Selenium, pandas, seaborn, matplotlib, folium 
<br><br><br>

## [크롤링 항목]<br><br>
1. 주간보호센터 이름
2. 정원
3. 현원
4. 주소 -> 경/위도로 전처리
5. 상주인구현황 -> 70세-100세 구/동별 인구합계로 
<br><br><br>

## [주의할 점]<br><br>
chromedriver 로 크롤링을 하기에, chromedriver와 사용자가 쓰고 있는 chrome 버전이 일치해야 돌아간다.
<br>
<br>
<br>

## [실행 파일 만드는 방법]<br><br>

(1) 초기 실행 파일 만들기 <br><br>
![image](https://user-images.githubusercontent.com/58064919/172084859-d886ede3-65f4-4c13-be16-4113ba8c9638.png)

(2) 마지막 줄에 깨알 icon을 추가해줍니다.<br><br>
![image](https://user-images.githubusercontent.com/58064919/172085287-2acaf6e8-1093-436b-a539-28108ad4c133.png)

(3) 수정된 파일을 다시 exe 파일로 구워주기 <br><br>
![image](https://user-images.githubusercontent.com/58064919/172085366-324dd071-c9f1-4073-a472-73caa7735a8d.png)
<br>
<br><br><br>

## [실행/결과 이미지]<br><br>

(1) 프로그램을 클릭하면 다음과 같은 창이 뜹니다. 프로그램이 작동 중에 있다는 뜻이니 건드리면 안됩니다.<br><br>
![image](https://user-images.githubusercontent.com/58064919/172086140-b93ed906-7437-49e6-8ef4-19a042677918.png)
<br><br><br>

(2) 결과 폴더입니다.<br><br>
![image](https://user-images.githubusercontent.com/58064919/172086070-7f9d0b9e-a6da-4543-8690-830cd0c77a6c.png)
<br><br><br>

(3) 결과 파일입니다.<br><br>
![image](https://user-images.githubusercontent.com/58064919/172086016-2f5c7644-41fe-462f-bd23-2e010bf5ceed.png)
<br><br><br>

(4) 5월상주인구현황.xlsx<br><br>
![image](https://user-images.githubusercontent.com/58064919/172086562-a48d0216-3afb-40d5-b5e2-f2e4e15e19ef.png)
<br><br><br>

(5) 6월_6일_방문요양 현황.xlsx<br><br>
![image](https://user-images.githubusercontent.com/58064919/172086665-5a9ca4bb-c5f5-4202-a9c7-58b611cc54f8.png)
<br><br><br>

(6) 6월_6일_주야간보호 현황.xlsx<br><br>
![image](https://user-images.githubusercontent.com/58064919/172086729-aff062b8-089c-4d27-bf1c-819e718701cb.png)
<br><br><br>

(7) 6월_6일_주야간보호 현황 그래프.<br><br>
![image](https://user-images.githubusercontent.com/58064919/172086763-f0820d61-cc05-4443-aee8-c71f0e2a8bdd.png)
<br><br><br>

(8) 주간보호/방문요양 지도.<br><br>
![image](https://user-images.githubusercontent.com/58064919/172086878-743b4b00-e637-4d2b-8a08-adb9bd7615e1.png)
<br><br><br>
