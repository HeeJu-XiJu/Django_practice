1. 프로젝트 생성
2. 앱생성/앱등록
3. 'base.html' 설정
4. 모델링/마이그레이션
5. Create
6. Read(All)
7. Read(1)
8. Delete
9. Update

## 정리
- ModelsForm에서 instance의 default값은 none
이때 instance의 값이 none이 아니여야 update를 함
```
def update(request, id):
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', id=article.id)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
    }
    return render(request, 'update.html', context)
```
따라서 `form = ArticleForm(request.POST, instance=article)`로 작성해야 update
instance 미지정 시 업데이트 전과 같은 정보 출력