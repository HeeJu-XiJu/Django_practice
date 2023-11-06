from django.shortcuts import render, redirect
from .models import Article, Comment
from .form import ArticleForm, CommentForm

# Create your views here.
def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }
    return render(request, 'index.html', context)


def detail(request, id):
    article = Article.objects.get(id=id)
    form = CommentForm()
    # 1. comments = Comment.objects.filter(article=article)
    # 2. comments = article.comment_set.all()
    # 3. HTML코드에서 2 사용

    context = {
        'article': article,
        'form': form,
        #'comments': comments,
    }
    return render(request, 'detail.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', id=article.id)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }

    return render(request, 'form.html', context)


def delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    return redirect('articles:index')


def update(request, id):
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', id=article.id)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
    }
    return render(request, 'form.html', context)


def comment_create(request, article_id):
    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)

        # article = Article.objects.get(id=article_id)
        # comment.article = article
        # comment.save()

        comment.article_id = article_id
        comment.save()

        return redirect('articles:detail', id=article_id)
    

def comment_delete(request, article_id, id):
    comment = Comment.objects.get(id=id)
    comment.delete()

    return redirect('articles:detail', id=article_id)