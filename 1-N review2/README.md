1. 프로젝트 생성
2. 앱생성/앱등록
3. 모델링/마이그레이션
4. 'base.html' 설정 및 Read(all)
5. Create
6. Read(1)
7. Comment Create
- `urls.py`
```
    path('<int:article_id>/comments/create/', views.comment_create, name='comment_create'),
```

- `views.py`
```
def comment_create(request, article_id):
    article = Article.objects.get(id=article_id)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.article = article
        comment.save()
        return redirect('articles:detail', id=article.id)
```