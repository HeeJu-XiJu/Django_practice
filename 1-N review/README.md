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

4. 모델링/마이그레이션
- `models.py`
```
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

class Comment(models.Model):
    comment = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
```

- 번역본 생성
```
python manage.py makemigrations
```

- DB에 반영
```
python manage.py migrate
```

- `admin.py`
```
from .models import Article, Comment
admin.site.register(Article)
admin.site.register(Comment)
```

- 관리자계정 생성
```
python manage.py createsuperuser
```

5. READ(ALL)
- `urls.py`
```
from . import views
path('', views.index, name='index'),
```

- `appname` - `templates` - `index.html`
```
{% extends 'base.html' %}

{% block body %}
    {% for article in articles %}
        <p>{{article.title}}</p>
        <hr>
    {% endfor %}
{% endblock %}
```

- `views.py`
```
def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }
    return render(request, 'index.html', context)
```