1. 프로젝트 생성
2. 앱생성/앱등록
3. 'base.html' 설정
4. Post 모델링/마이그레이션
- `ImageField`사용을 위해 `pip install pillow`

5. Post Read(All)
- `base.html`
```
    {% include '_nav.html' %}
    <div class="container">
        {% block body %}
        {% endblock %}
    </div>
```

- `_nav.html` 구성

- `settings.py`
```
# 업로드한 사진을 저장할 위치
MEDIA_ROOT = BASE_DIR / 'media'

# 미디어 경로를 처리할 URL
MEDIA_URL = '/media/'
```

- `insta` - `urls.py`
```
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

- `posts` - `urls.py`
```
from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
]
```

- `views.py`
```
def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)
```

- `index.html`
```
{% extends 'base.html' %}

{% block body %}
    {% for post in posts %}
        {% include '_card.html' %}
    {% endfor %}
{% endblock %}
```

- `_card.html`
```
<div class="card">
    <div class="card-header">작성자</div>
    <img src="{{ post.image.url }}" alt="">
    <div class="card-body">
        <p class="'card-text">{{ post.content }}</p>
    </div>
</div>
```