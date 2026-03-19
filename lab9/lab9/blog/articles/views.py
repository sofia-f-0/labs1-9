
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Article

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})


def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404("Статья не найдена")


def create_post(request):
    if not request.user.is_authenticated:
        raise Http404("Доступ запрещён")
    
    if request.method == "POST":
        form = {
            'title': request.POST.get('title', ''),
            'text': request.POST.get('text', '')
        }
        if form['title'] and form['text']:
            if Article.objects.filter(title=form['title']).exists():
                form['errors'] = "Статья с таким названием уже существует"
                return render(request, 'create_post.html', {'form': form})
            article = Article.objects.create(
                title=form['title'],
                text=form['text'],
                author=request.user
            )
            return redirect('get_article', article_id=article.id)
        else:
            form['errors'] = "Не все поля заполнены"
            return render(request, 'create_post.html', {'form': form})
    else:
        return render(request, 'create_post.html', {})


def register(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        password_confirm = request.POST.get('password_confirm', '')

        errors = {}

        if not username:
            errors['username'] = "Имя пользователя не может быть пустым"
        elif User.objects.filter(username=username).exists():
            errors['username'] = "Пользователь с таким именем уже существует"

        if not email:
            errors['email'] = "Email не может быть пустым"
        elif User.objects.filter(email=email).exists():
            errors['email'] = "Пользователь с таким email уже зарегистрирован"

        if not password:
            errors['password'] = "Пароль не может быть пустым"
        elif password != password_confirm:
            errors['password_confirm'] = "Пароли не совпадают"

        if not errors:
            user = User.objects.create_user(username, email, password)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('archive')
            else:
                return render(request, 'register.html', {'errors': {'auth': "Ошибка входа после регистрации"}})
        else:
            return render(request, 'register.html', {'errors': errors, 'data': request.POST})
    else:
        return render(request, 'register.html', {})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('archive')
        else:
            return render(request, 'login.html', {
                'errors': {'auth': "Неверное имя пользователя или пароль"},
                'data': request.POST
            })
    else:
        return render(request, 'login.html', {})


def user_logout(request):
    logout(request)
    return redirect('archive')