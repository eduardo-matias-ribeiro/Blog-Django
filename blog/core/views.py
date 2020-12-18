from django.db.models.functions import Lower
from django.shortcuts import render,redirect, get_object_or_404
from .models import Post
from .forms import PostModelForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User




def index(request):
    articles = Post.objects.all().order_by(Lower('id').asc())
    context = {
        'articles': articles
    }
    return render(request, 'index.html', context)


@login_required
def article(request):
    form = PostModelForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            art = form.save(commit=False)
            art.author = request.user
            art.save()
            messages.success(request, 'Artigo publicado com sucesso.')
            return redirect('index')
        else:
            messages.error(request, 'Erro ao publicar artigo.')

    context = {
        'form': form,
    }
    return render(request, 'articles/index.html', context)

def detail(request,pk):
    article = Post.objects.get(id=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)

@login_required
def edit(request, pk):
    article = Post.objects.get(id=pk)
    form = PostModelForm(request.POST or None, instance=article)

    if form.is_valid():
        form.save()
        return redirect('index')

    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/edit.html', context)

@login_required
def delete(request, pk):
    article = Post.objects.filter(id=pk).delete()
    return redirect('index')


def myArticles(request):
    articles = Post.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/my-articles.html', context)
