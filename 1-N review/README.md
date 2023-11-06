1. 기본 프로젝트 생성
- `.gitignore`, `README.md`
- project 생성
```
django-admin startproject <pjtname> .
```
- 가상환경 설정
```
python -m venv venv
```
- 가상환경 실행
```
source venv/bin/activate
```
- django 설치
```
pip install django
```
- 서버 실행
```
python manage.py runserver
```

2. 앱 생성/앱 등록
- 앱 생성
```
django-admin startapp <appname>
```
- 앱 등록
`setting.py`의 `INSTALLED_APPS`의 `<appname>`

3. `base.html` 세팅
- 최상위 `templates` - `base.html`
```
<body>
    {% block body %}
    {% endblock %}
</body>
```

- `setting.py`
```
'DIRS': [BASE_DIR, 'templates'],
```

- `pjtname` - `urls.py`
```
from django.urls import path, include
path('articles/', include('articles.urls')),
```