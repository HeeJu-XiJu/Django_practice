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

app_name = 'articles'

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

5. Signup
- `forms.py`
```
from .models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields
```

- `auth urls.py`
```
path('accounts/', include('accounts.urls')),
```

- `accounts urls.py`
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

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'signup.html', context)
```

- `signup.html`
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

6. Login
- `forms.py`
```
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
class CustumAuthenticationForm(AuthenticationForm):
    pass
```

- `urls.py`
```
path('login/', views.login, name='login'),
```

- `views.py`
```
def login(request):
    if request.method == 'POST':
        form = CustumAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = CustumAuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)
```

- `login.html`
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

7. Logout
- `urls.py`
```
    path('logout/', views.logout, name='logout'),
```

- `views.py`
```
def logout(request):
    auth_logout(request)
    return redirect('accounts:login')
```