1. `.gitignore`, `README.md` 추가

2. 프로젝트 생성
```
django-admin startproject <pjtname> .
(pjtname : crud)
```

3. 가상환경 설정
```python
python -m venv venv
```

4. 가상환경 활성화/비활성화
```python
source venv/bin/activate

deactivate
```

5. 가상환경 내부에 django 설치
```
pip install django
```

`pip list`로 확인

6. 서버 실행 확인
```python
python manage.py runserver
```

7. 앱 생성
```
django-admin startapp <appname>
(appname : posts)
```

8. 앱 등록
`settings.py`의 `INSTALLED_APPS`에 `<appname>` 등록

9. `urls.py`
```
from django.urls import path
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
]
```

10. `view.py`
```
def index(request):
    return render(request, 'index.html')
```

11. `templates` 폴더 -> `index.html` 생성

12. 모델 정의(`models.py`)
```python
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
```

13. 번역본 생성
```python
python manage.py makemigrations
```

14. DB에 반영
```python
python manage.py migrate
```