1. 프로젝트 생성
2. 앱생성/앱등록
3. 'base.html' 설정
4. Post, Comment, User 모델링/마이그레이션
Post : Comment = 1 : N
User : Post = 1 : N
Post : Comment = 1 : N

N의 역할을 하는 model에 foreignkey 지정
위에서 1의 역할을 하는 model에 자동으로 model_id 컬럼 생성
N의 역할을 하는 model에 자동으로 model_set 컬럼 생성

AbstractUser 기본 모델
![AbstracUser 기본모델](/auth%20review2/posts/reference/image.png)

AbstracUser을 불러오는 방법 : get_user_model

5. Signup
- `forms.py`
```
from dajngo.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields
```


6. Login
- `forms.py`
```
class CustomAuthenticationForm(AuthenticationForm):
        pass
```

- `views.py`
```
def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            next_url = request.GET.get('next')
            return redirect(next_url or 'posts:index')
    else:
        form = CustomAuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'form.html', context)
```

- `base.html`
```
            <div class="navbar-nav">
              {% if user.is_authenticated %}
```


7. Logout

8. Post Create

9. Post Read(All)

10. Post Read(1)

11. Comment Create
- `views.py`
```
def comment_create(request, post_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user_id = request.user.id
        comment.post_id = post_id
        comment.save()
        return redirect('posts:detail', post_id=post_id)
```

12. Comment Read