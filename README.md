# Anaconda 환경설정

- env 생성
conda create -n ex_env python=3.11.4
- env 활성화
conda activate ex_env

# 기록

django_env 라는 이름으로 conda 환경 생성함
postgresSQL 설치해서 원격 접속해봄

<https://velog.io/@new_wisdom/Django-3-Model-MTV-%ED%8C%A8%ED%84%B4> - 얘 할 차례임

단비 기술스택
• Celery, Redis, Apache Sentry, Travis CI, Jenkins, Git, Docker, PostgreSQL, DRF(Django REST framework), Django, Amazon Web Services(AWS)

# 모델 수정하면 해줘야 하는거

python manage.py makemigrations  - 모델의 변경 사항을 감지하여 데이터베이스 마이그레이션 파일을 생성합니다.
python manage.py migrate - 이 마이그레이션 파일들을 사용하여 데이터베이스의 스키마를 변경합니다.

python manage.py runserver

python manage.py makemigrations your_app_name - 마이그레이션 파일 지워버렸을때 대책