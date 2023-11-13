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


9. Accounts Signup
- `_nav.html`
```
          <a class="nav-link" href="{% url 'accounts:signup' %}">Signup</a>
```

- `insta-urls.py`
```
    path('accounts/', include('accounts.urls')),
```

- `accounts-urls.py`
```
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
]
```

- `views.py`
```
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts_form.html', context)
```

- `forms.py`
```
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'profile_image',)
```

- `settings.py`-`INSTALLED_APPS`-'bootstrap5'

- `accounts_form.html`
```
{% extends 'base.html' %}
{% load bootstrap5 %}

{% block body %}
    <form action="" method="POST" enctype="multipart/form-data">
        {% csrf_token %}
        {% bootstrap_form form %}
        <input type="submit">
    </form>
{% endblock %}
```

10. Login
- `_nav.html`
```
          <a class="nav-link" href="{% url 'accounts:login' %}">Login</a>
```

- `urls.py`
```
    path('login/', views.login, name='login'),
```

- `forms.py`
```
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    pass
```

- `views.py`
```
def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('posts:index')
    else:
        form = CustomAuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts_form.html', context)
```


11. Logout, Create 수정
#### Logout
- `_nav.html`
```
        <div class="navbar-nav">
          {% if user.is_authenticated %}
            <a class="nav-link active" aria-current="page" href="{% url 'posts:create' %}">Create</a>
            <a class="nav-link" href="{% url 'accounts:logout' %}">Logout</a>
          {% else %}
            <a class="nav-link" href="{% url 'accounts:signup' %}">Signup</a>
            <a class="nav-link" href="{% url 'accounts:login' %}">Login</a>
          {% endif %}
        </div>
```

- `urls.py`
```
    path('logout/', views.logout, name='logout'),
```

- `views.py`
```
def logout(request):
    auth_logout(request)
    return redirect('posts:login')
```

#### Create 수정
- `forms.py`
```
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('content', 'image', )
```

- `views.py`
```
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:index')
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'form.html', context)
```

- `_card.html`
```
    <div class="card-header">{{ post.user }}</div>
```


12. Profile
- `_card.html`
```
    <div class="card-header">
        <a href="{% url 'accounts:profile' username=post.user %}" class="text-reset text-decoration-none">
        {{ post.user }}
        </a>
    </div>
```

- `urls.py`
```
    path('<str:username>/', views.profile, name='profile'),
```

- `views.py`
```
def profile(request, username):
    user_info = User.objects.get(username=username)
    context = {
        'user_info': user_info,
    }
    return render(request, 'profile.html', context)
```


13. Like 모델링
- `models.py`
```
    like_users = models.ManyToManyField(settings.AUTH_USER_MOEL, related_name='like_posts')
```

- User : Post_user_set, Post_like_posts_set
- Post : User_id,


14. Like
- `_card.html`
```
    <div class="card-body">
        <a href="{% url 'posts:likes' id=post.id %}" class="text-reset text-decoration-none">
            {% if user in post.like_users.all %}
                <i class="bi bi-heart-fill" style="color:red"></i>
            {% else %}
                <i class="bi bi-heart"></i>
            {% endif %}
        </a> {{ post.like_users.all|length }}명이 좋아합니다.
        <p class="'card-text">{{ post.content }}</p>
    </div>
```

- `urls.py`
```
    path('<int:id>/likes', views.likes, name='likes'),
```

- `views.py`
```
@login_required
def likes(request, id):
    user = request.user
    post = Post.objects.get(id=id)

    if user in post.like_users.all():
        post.like_users.remove(user)
    else:
        post.like_users.add(user)
    return redirect('post:index')
```


15. Follow
- `models.py`
```
    followings = models.ManyToManyField('self', related_name='followers', symmetrical=False)
```

- `profile.html`
```
        <div class="col-3">{{ user_info}}</div>
            <!-- user : 현재 로그인한 유저 / user_info : 현재 프로필페이지 유저 -->
            {% if user != user_info %}
            <div class="col-4">
                {% if user in user_info.followers.all %}
                    <a href="{% url 'accounts:follows' username=user_info %}" class="btn btn-primary">following</a>
                {% else %}
                    <a href="{% url 'accounts:follows' username=user_info %}" class="btn btn-secondary">follow</a>
                {% endif %}
            </div>
            {% endif %}
            <a href="" class="btn btn-light">follow</a>
            <div class="row">
                <div class="col">게시물 {{ user_info.post_set.all|length }}</div>
                <div class="col">팔로워 {{ user_info.followers.all|length }}</div>
                <div class="col">팔로잉 {{ user_info.followings.all|length }}</div>
            </div>
        </div>
```

- `urls.py`
```
    path('<str:username>/follows/', views.follows, name='follows'),
```

- `views.py`
```
def follows(request, username):
    me = request.user
    you = User.objects.get(username=username)

    if you in me.followings.all():
        me.followings.remove(you)
    else:
        me.followings.add(you)
    return redirect('accounts:profile', username=username)
```

16. requirements.txt 추가
- `pip freeze >> requirements.txt`

- 같은 버전으로 설치할 때
`pip install -r requirements.txt`


17. 기본이미지 설정(ex. admin 계정)
- `profile.html`
```
        <div class="col-4">
            {% if user_info.profile_image %}
                <img src="{{ user_info.profile_image.url }}" alt="" class="rounded-circle img-fluid">
            {% else %}
                <img src="/insta review/media/profile/default.png" alt="" class="rounded-circle img-fluid">
            {% endif %}
        </div>
```

- `_card.html`
```
    <div class="card-header">
        {% if post.user.profile_image %}
        <img src="{{  post.user.profile_image.url  }}" alt="">
        {% else %}
        <img src="/insta review/media/profile/default.png" alt="">
        {% endif %}
        <a href="{% url 'accounts:profile' username=post.user %}" class="text-reset text-decoration-none">
        {{ post.user }}
        </a>
    </div>
```