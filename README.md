# Anniversary Notification

**i-Keeper 팀 프로젝트 "오늘은 무슨 날?" 의 백엔드 리포지토리**

[프론트엔드](https://github.com/)

# 

## 프로젝트 설명
* 기본 캘린더에서 제공하는 기념일 외의 다양한 기념일들과,<br>사람들이 잘 모르고 지나가는 기념일에 대한 정보를 제공하는 어플리케이션

## 프로젝트 개요 
* **10~30대의 모바일 OS 점유율을 고려하여 크로스플랫폼 프레임워크인 React-Native를 채택**

* 해당 일자의 기념일과 그 날에 일어났던 사건 등을 푸시알림으로 전송

* 기념일과 관련한 기사를 볼 수 있는 웹뷰 페이지 구현

* 프론트엔드
    * 각 날짜의 기념일과 사건의 정보를 제공하는 캘린더 제작
    * 당일의 기념일과 사건 푸시알림 기능 구현
    * 해당 날과 관련된 기사를 제공하는 WebView 제작

* 백엔드
    * Python의 Flask 프레임워크를 사용하여 Api 제작
    * [행정안전부](https://www.mois.go.kr/frt/sub/a06/b08/nationalHoliday_3/screen.do)의 기념일 정보를 JSON으로 변환
    * 오픈위키의 데이터베이스 덤프를 파싱하여 JSON으로 변환 후, 민감정보 필터링

## 개요
* 팀명 : 오늘은 무슨 날?
* 인원 : 4명
* 기간 : 2022.09.28 ~ 2023.02.01
* 개발 환경 : React Native 0.68.2, TypeScript 6.10.4, Python3 3.10, Flask 2.1.2
* 협업 툴 : Discord, Github
* 에디터 : VSCode
* 클라우드서버 : PythonAnywhere
* 노션페이지 : [AnniversaryNoti](https://gray-beginner-bbf.notion.site/React-Native-6b971b37929d480b904fec8f392b135d)
* 시연 영상 : [Youtube](https://www.youtube.com/)

## Task 분배
| 이름        | Task 목록 |
| ----------- | ------------------------------------------------------------- |
| 신세미         | 캘린더 액티비티, JSON 데이터 추출 |
| 윤선빈         | 푸시알림 구현, WebView 제작 |
| 이상원         | 행정안전부 데이터 JSON변환, 데이터 필터링 |
| 차성겸         | 오픈위키 데이터 JSON변환, Api서버 구축 |

## 어플리케이션 결과
**여기에 스크린샷이 들어가야 함**

## API 결과
| 종류 | 설명 | Method | Path | Parameter | return |
| ---- | ---- | ------ | ---- | --------- | ------ |
| 행정안전부 | 전체 정보 조회 | GET | /annijson | | JSON |
| 행정안전부 | 날짜 조회 | GET, POST | /api/gov | {"month":mm, "date":dd} | JSON |
| 오픈위키 | 날짜 조회 | GET, POST | /api/wiki | {"month":mm, "date":dd} | JSON |

<img width="653" alt="govtest" src="https://user-images.githubusercontent.com/102679480/215712322-16038cd7-1f08-43f2-8049-90679aa59cbe.png" width="50%" height="50%">
<img width="912" alt="wikiTest" src="https://user-images.githubusercontent.com/102679480/215712348-2332f8af-d000-43f9-9702-f10311a5b2b5.png" width="50%" height="50%">



## 백엔드 코멘트 **프론트는 프론트 코멘트 적어주셈 없으면 안적어도됨**
* 
