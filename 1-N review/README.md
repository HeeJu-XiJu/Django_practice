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


6. READ(1)
- `urls.py`
```
app_name = 'articles'
path('<int:id>', views.detail, name='detail'),
```

- `index.html`
```
        <a href="{% url 'articles:detail' id=article.id %}">detail</a>
```

- `detail.html`
```
{% extends 'base.html' %}

{% block body %}
    <h1>{{ article.title }}</h1>
    <p>{{ article.content }}</p>
{% endblock %}
```

- `views.py`
```
def detail(request, id):
    article = Article.objects.get(id=id)

    context = {
        'article': article,
    }
    return render(request, 'detail.html', context)
```

7. CREATE
- `form.py`
```
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
```

- `index.html`
```
<a href="{% url 'articles:create' %}">create</a>
```

- `urls.py`
```
path('create/', views.create, name='create'),
```

- `form.html`
```
{% extends 'base.html' %}

{% block body %}
    <form action="" method="POST">
        {% csrf_token %}
        {{ form }}
        <input type="submit">
    </form>
{% endblock %}
```

- `views.py`
```
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', id=article.id)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }

    return render(request, 'form.html', context)
```