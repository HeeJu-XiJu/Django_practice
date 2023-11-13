1. 프로젝트 생성
2. 앱생성/앱등록
3. 'base.html' 설정
4. Post, Comment, User 모델링/마이그레이션
Post : Comment = 1 : N
User : Post = 1 : N
Post : Comment = 1 : N

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