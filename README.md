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

3. `base.html`작성
- 최상위 폴더 `templates`생성 후 `base.html`생성
```
<body>
    {% block body %}
    
    {% endblock %}
</body>
```

- `settings.py`의 `TEMPLATES`
```
'DIRS': [BASE_DIR / 'templates'],
```

- `<pjtname>`의 `urls.py`
```
from django.urls import path, include

    path('articles/', include('articles.urls')),

```

- `<appname>`의 `urls.py`
```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]
```

- `views.py`
```
def index(request):
    return render(request, 'index.html')
```

- `<appname>`의 `templates`생성 후 `index.html`
```
{% extends 'base.html' %}

{% block body %}
    <h1>index</h1>
{% endblock %}
```

4. 모델링/마이그레이션
- `models.py`
```
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
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
from .models import Article
admin.site.register(Article)
```

- 관리자 계정 생성
```
python manage.py createsuperuser
```

- migratite 이후 model을 수정할 시, db.sqlite3와 migrations파일을 삭제 후 재실행
(오류화면 table articles_article has no column named title)

5. READ(ALL)
`views.py`
```
from .models import Article

def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }
    return render(request, 'index.html', context)
```

`index.html`
```
{% block body %}
    <h1>index</h1>

    {% for article in articles %}
        <p>{{ article.title }}</p>
        <p>{{ article.content }}</p>
        <hr>
    {% endfor %}
{% endblock %}
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

- `views.py`
```
def detail(request, id):
    article = Article.objects.get(id=id)

    context = {
        'article': article,
    }
    return render(request, 'detail.html', context)
```

`detail.html`
```
{% extends 'base.html' %}

{% block body %}

    <p>{{ article.title }}</p>
    <p>{{ article.content }}</p>
    <p>{{ article.created_at }}</p>

{% endblock %}
```

7. CREATE
- `index.html`
```
    <a href="{% url 'articles:create' %}">create</a>
```

- `urls.py`
```
    path('create/', views.create, name='create'),
```

- `forms.py`
```
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Articlefields = '__all__'
```

- `create.html`
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
from django.shortcuts import render, redirect
from .forms import ArticleForm

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:index')
        else:
            context = {
                'form': form,
            }
            return render(request, 'create.html', context)
    else:
        form = ArticleForm()

        context = {
            'form': form,
        }

        return render(request, 'create.html', context)
```

8. CREATE(2)
`views.py`
```
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()

    context = {
        'form': form,
    }

    return render(request, 'create.html', context)
```

9. DELETE
- `index.html`
```
        <a href="{% url 'articles:delete' id=article.id %}">delete</a>
```

- `urls.html`
```
    path('<int:id>/delete/', views.delete, name='delete'),
```

- `views.py`
```
def delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    return redirect('articles:index')
```

10. UPDATE
`index.html`
```
        <a href="{% url 'articles:update' id=article.id %}">update</a>
```

`urls.py`
```
        path('<int:id>/update/', views.update, name='update'),
```

`update.html`
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

`views.py`
```
def update(request, id):
    article = Article.objects.get(id=id)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', id=article.id)
    else:
        form = ArticleForm(instance=article)

    context = {
        'form': form,
    }

    return render(request, 'update.html', context)
```

11. `create.html`, `update.html` 통합
- `create.html`, `update.html` 삭제
- `form.html`생성 
- `views.py`
`create.html`, `update.html` => `form.html`로 수정