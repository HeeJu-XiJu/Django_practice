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

## accounts
3. 모델링/마이그레이션
- `models.py`
```
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```

- `settings.py`
```
AUTH_USER_MODEL = 'accounts.User'
```

- `admin.py`
```
from .models import User

admin.site.register(User)
```

- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py createsuperuser`

4. Index
- `auth urls.py`
```
from django.urls import path, include
    path('articles/', include('articles.urls')),
```

- `articles urls.py`
```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

- `views.py`
```
def index(request):
    return render(request, 'index.html')
```

- `base.html`
```
<body>
    {% block body %}
    {% endblock %}
</body>
```

- `index.html`
```
{% extends 'base.html' %}

{% block body%}
    <h1>index</h1>
{% endblock %}
```