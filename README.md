# 어플리케이션 스펙

- backend django
- frontend react
- db postgresSQL

## Anaconda 환경설정

- env 생성
conda create --prefix C:\myenvs\myenv python=3.11.4
- env 활성화
conda activate C:\myenvs\myenv
- env 목록 확인
conda info --env

현재 환경에서는

conda activate C:\dev\danbi

## 기록

django_env 라는 이름으로 conda 환경 생성함
postgresSQL 설치해서 원격 접속해봄

<https://velog.io/@new_wisdom/Django-3-Model-MTV-%ED%8C%A8%ED%84%B4> - 얘 할 차례임

단비 기술스택
• Celery, Redis, Apache Sentry, Travis CI, Jenkins, Git, Docker, PostgreSQL, DRF(Django REST framework), Django, Amazon Web Services(AWS)

## 추가적인 app 생성

python manage.py startapp app_name

seriailizers.py
urls.py 복사해서 넣어주기

settings.py -> INSTALLED_APPS에 app_name 추가

edu_django.urls.urlpatterns에 url추가

## 모델 수정하면 해줘야 하는거

python manage.py makemigrations  - 모델의 변경 사항을 감지하여 데이터베이스 마이그레이션 파일을 생성합니다.
python manage.py migrate - 이 마이그레이션 파일들을 사용하여 데이터베이스의 스키마를 변경합니다.

python manage.py runserver

python manage.py makemigrations your_app_name - 마이그레이션 파일 지워버렸을때 대책

## pip 관리

pip install -r requirements.txt

## 문뜩 생각해본거

가사 프리랜서들이 매칭할 수 있는 앱

청소해주기 원하는 부위를 찍어 올리면 그걸 프리랜서 가사도우미들이 보고 before-after로 비교샷도 찍을 수 있는 뭐 그런 플랫폼?

## extension

eslint
markdownlint

## bat 작성법

@echo off
cd /D C:\dev\edu_django\jango_edu\

%windir%\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy ByPass -NoExit -Command "& 'C:\ProgramData\anaconda3\shell\condabin\conda-hook.ps1' ; conda activate 'C:\ProgramData\anaconda3' ; conda activate C:\dev\danbi ; python manage.py runserver"

Anaconda Powershell Prompt -> 속성 -> 대상 내용 복사해서 위에 콘다 관련 내용이랑 변환시키면 됨

@echo off
cd /D C:\Developers\django_edu\jango_edu\
%windir%\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy ByPass -NoExit -Command "& 'C:\Users\akuo\anaconda3\shell\condabin\conda-hook.ps1' ; conda activate django ; python manage.py makemigrations ; python manage.py migrate"

모델 수정후에 동작시키는거

## frontend 세팅

node.js 18.4.0
npm install -g create-react-app

- 그냥 실행하려면?

npm start
