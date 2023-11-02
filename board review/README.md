1. `.gitignore`, `README.md` 작성

2. 프로젝트 생성
```
django-admin startproject <pjtname> .
```

3. 가상환경 설정
```python
python -m venv venv
```

4. 가상환경 활성화
```python
source venv/bin/activate
```

5. django 설치
```
pip install django
```

6. 서버 실행 확인
```python
python manage.py runserver
```

7. 앱 생성
```
django-admin startapp <appname>
```

8. 앱 등록 \
`setting.py`의 `INSTALLED_APPS` `<appname>`등록

9. 공통 base.html 작성
`setting.py` - `TEMPLATES`
```
'DIRS': [BASE_DIR / 'templates'],
```

`board`-`urls.py`
```
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
]
```

`<appname>`의 `urls.py` 생성 후
```
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
]
```

`views.py`
```
def index(request):
    return render(request, 'index.html')
```

`templates`생성 후 
`base.html`
```
<body>
    <h1>base</h1>
    {% block body %}

    {% endblock %}
</body>
```

`index.html`
```
{% extends 'base.html' %}

{% block body %}
    <h1>안녕하세요</h1>
{% endblock %}
```
