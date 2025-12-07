from django.shortcuts import render, redirect
from django.http import Http404
from .models import Article


def create_post(request):
    if request.user.is_anonymous:
        raise Http404 

    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        text = request.POST.get("text", "").strip()

        if not title or not text:
            return render(request, 'create_post.html', {
                'form': {
                    'title': title,
                    'text': text,
                    'errors': 'Не все поля заполнены'
                }
            })

        if Article.objects.filter(title=title).exists():
            return render(request, 'create_post.html', {
                'form': {
                    'title': title,
                    'text': text,
                    'errors': 'Статья с таким заголовком уже существует'
                }
            })

        article = Article.objects.create(
            title=title,
            text=text,
            author=request.user
        )

        return redirect('get_article', article_id=article.id)

    else:
        return render(request, 'create_post.html', {})