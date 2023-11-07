1. 프로젝트 생성
- `.gitignore`, `README.md`
- `django-admin startproject <pjtname> .`
- `python -m venv venv`
- `source venv/bin/activate`
- `pip install django`

2. 앱생성/앱등록, base.html등록
- `django-admin startapp <appname>`
- `setting.py`-`INSTALLED_APPS`-`<appname>`등록
- `base.html`생성
- `setting.py`-`'DIRS': [BASE_DIR, 'templates'],`
