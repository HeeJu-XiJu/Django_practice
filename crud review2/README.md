1. 프로젝트 생성
2. 앱생성/앱등록
3. 모델링/마이그레이션
4. Read(All)
5. Read(1)
6. Create
- New(정보를 기입하는 종이)
- Create(정보를 저장)
- `urls.py`
```
    path('posts/new/', views.new, name='new'),
    path('posts/create/', views.create, name='create'),
```

- `views.py`
```
def new(request):
    return render(request, 'new.html')


def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    post = Post()
    post.title = title
    post.content = content
    post.save()

    return redirect(f'/posts/{post.id}')
```

- `new.html`
```
<body>
    <h1>new</h1>
    <form action="/posts/create/">
        <label for="title">title</label>
        <input type="text" id="title" name="title">
        <label for="content">content</label>
        <textarea name="content" id="content" cols="30" rows="10"></textarea>
        <input type="submit">
    </form>
</body>
```

- `index.html`
```
    <a href="/posts/new">create</a>
```


7. Delete
- `index.html`
```
    <a href="/posts/{{post.id}}/delete/">delete</a>
```


8. Update
- `views.py`
```
def update(request, id):
    title = request.GET.get('title')
    content = request.GET.get('content')

    post = Post.objects.get(id=id)
    post.title = title
    post.content = content
    post.save()
    return redirect(f'/posts/{post.id}')
```