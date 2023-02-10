# 나무위키 파싱

#### 나무위키는 [데이터베이스 덤프](https://blog.naver.com/livetrack/222326092570)를 제공하므로 크롤링 대신 덤프 분석으로 JSON 데이터를 수집하기로 결정했다.

## 정보
* 언어 : Python3
* 사용 모듈 : [namuwiki.extractor](https://github.com/jonghwanhyeon/namu-wiki-extractor)

## 과정
* 구글 드라이브로 덤프 업로드 후 구글 코랩에서 마운트
* namuwiki.extractor 모듈을 사용하여 정제된 텍스트 추출
* 각 일별 문서의 데이터를 담은 txt 파일을 작성
    * 365개의 모든 문서의 형식이 동일하지 않아 직접 구문분석을 진행하였음
* txt 파일을 JSON으로 변환 후 최종 병합

## 결과
[AnniversaryNoti.json](https://github.com/csk200387/AnniversaryNoti/blob/main/Wiki/Anniversary.json)

## 추가 개선사항
* 데이터 진위여부 확인
    * 오픈위키 특성상 이상한 정보가 포함돼있을 가능성 높음
* 데이터 추가 