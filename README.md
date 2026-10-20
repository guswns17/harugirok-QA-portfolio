# 하루기록 QA 포트폴리오

## 프로젝트 소개
기록 관리 웹사이트(https://guswns17.github.io/harugirok/)를
수동 테스트하고, Python + Selenium으로 자동화했습니다.

## 테스트 범위
- 메뉴 이동 (기록, 통계, 설정)
- 글 작성 및 저장

## 사용 도구
Python, Selenium, Chrome

## 실행 방법
1. pip install selenium
2. python automation/harugirok_test.py

## 결과
자동화 테스트 4건 실행, 4건 통과

## 문제 해결 사례
스크롤 애니메이션 때문에 저장 버튼 클릭이 실패했고,
원인을 분석해 애니메이션을 끄는 방식으로 해결했습니다.
