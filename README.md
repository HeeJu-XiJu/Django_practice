1. 기본프로젝트 구성
- `.gitignore`, `README.md` 생성

- 프로젝트 작성
```
django-admin startproject <pjtname> .
```

- 가상환경 설정
```
python -m venv venv
```

- 가상환경 활성화
```
source venv/bin/activate
```

- django 설치
```
pip install django
```

- 서버 실행 확인
```
python manage.py runserver
```

2. 앱 생성/앱 등록
- 앱 생성
```
django-admin startapp <appname>
```

- 앱 등록
`setting.py`의 `INSTALLED_APPS`에 app 등록

