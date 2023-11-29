from django.shortcuts import render, get_object_or_404, redirect 
from django.http import HttpResponse, HttpResponseNotFound
from .models import Women, Category


# Create your views here.


# menu было реализовано при помощи пользовательского тега 

def show_post(request, post_slug): # функции заглушки для вывода страниц
    post = get_object_or_404(Women, slug=post_slug)

    context = {
        'post': post,
        'title': post.title, 
        'cat_selected': post.cat_id, 
    }

    return render(request,'women/post.html', context=context) 


# функция вывода постов выбранной категории, 
# где передается id выбранной каторегории
# и на основе нее создается sql запрос для фильтрации 

def show_category(request, cat_slug): 
    category = get_object_or_404(Category, slug=cat_slug) # запрос на получения категории, 

    posts = Women.objects.filter(cat_id=category.pk) # запрос в базу с фильтрацией и учетом id категории 
    #cats = Category.objects.all()   
    # проверка на наличие постов в выбранной категории, 
    # если их нет то выдает ошибку page_not_found_404

    # создание переменной для передачи информации
    context = {
        'posts':posts,
        'title':'Отображение по рубрикам',
        'cat_selected': category.pk,
    }
    return render(request, 'women/index.html', context=context)

    


def addpage(request):
    return HttpResponse('Добавить статью')
def login(request):
    return HttpResponse('login')
def contact(request):
    return HttpResponse('contact')

def categories(request, catid):
    
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{catid}</p>')
    
def index(request):
    posts = Women.objects.all() # обращение к классу Women и вывод всех экземпляров класса
    # cats = Category.objects.all() p.s. перенесли в теги в templates django 
    # # обращение к классу Category и вывод всех экземпляров класса
    # Создание переменной context для передачи информации в html макет
    context = {
        'posts':posts,
        'title':'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=context)

def about(request): 
    return render(request, 'women/about.html', {'title': 'О сайте'})


# фунция для вывода ошибки page_not_found_404 (требует исправления)
def pageNotFound(request, exeption):
    return HttpResponseNotFound('<h1>КОД 404 Страница не найдена!</h1>')

