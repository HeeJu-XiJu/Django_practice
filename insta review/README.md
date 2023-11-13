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

6. Post Create
- `_nav.html`
```
          <a class="nav-link active" aria-current="page" href="{% url 'posts:create' %}">Create</a>
```

- `urls.py`
```
    path('create/', views.create, name='create'),
```

- `forms.py`
```
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
```

- `views.py`
```
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'form.html', context)
```

- `form.html`
```
{% extends 'base.html' %}

{% block body %}
<form action="" method = 'POST' enctype="multipart/form-data">
    {% csrf_token %}
    {{ form }}
    <input type="submit">
</form>    
{% endblock %}
```

7. Image Resize 기능 추가
- `pip install django-resized`

- `models.py`
```
from django_resized import ResizedImageField

class Post(models.Model):
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    # image = models.ImageField(upload_to='image/%Y/%m')
    image = ResizedImageField(
        size=[500, 500],
        crop=['middle', 'center'],
        upload_to='image/%Y/%m'
    )
```

- 마이그레이션


8. Accounts 모델링
- `accounts-models.py`
```
class User(AbstractUser):
    profile_image = ResizedImageField(
        size=[500, 500],
        crop=['middle', 'center'],
        upload_to='profile'
    )
```

- `settings.py`
```
AUTH_USER_MODEL = 'accounts.User'
```

-  `posts-models.py`
```
class Post(models.Model):
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    # image = models.ImageField(upload_to='image/%Y/%m')
    image = ResizedImageField(
        size=[500, 500],
        crop=['middle', 'center'],
        upload_to='image/%Y/%m'
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```

- db삭제 후 마이그레이션