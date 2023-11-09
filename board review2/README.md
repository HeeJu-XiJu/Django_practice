1. 프로젝트 생성
2. 앱생성/앱등록
3. 모델링/마이그레이션
4. `base.html`설정
5. Read(All)
6. Read(1)
7. Create
- `views.py`
```
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article()
    article.title = title
    article.content = content
    article.save()
    return redirect('articles:detail', id=article.id)
```

- `new.html`
```
    <form action="{% url 'articles:create' %}" method="POST">
        {% csrf_token %}
        <label for="title">title</label>
        <input type="text" id="title" name="title" method="POST">
        <label for="content">content</label>
        <textarea name="content" id="content" cols="30" rows="10"></textarea>
        <input type="submit">
    </form>
```