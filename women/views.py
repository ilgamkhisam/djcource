from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Women, Category


# Create your views here.

# 1 из видов создания меню для сайта где в макете будут выводить через итератор

menu = [{'title':'О сайте', 'url_name':'about'},
        {'title':'Добавить статью', 'url_name':'addpage'},
        {'title':'Обратная связь', 'url_name':'contact'},
        {'title':'Войти', 'url_name':'login'},
] 

def show_post(request, post_id): # функции заглушки для вывода страниц
    return HttpResponse(f'{post_id}-ID статьи')

# функция вывода постов выбранной категории, 
# где передается id выбранной каторегории
# и на основе нее создается sql запрос для фильтрации 

def show_category(request, cat_id): 
    posts = Women.objects.filter(cat_id=cat_id) # запрос в базу с фильтрацией и учетом id категории 
    cats = Category.objects.all()   
    
    # проверка на наличие постов в выбранной категории, 
    # если их нет то выдает ошибку page_not_found_404
    if len(posts) == 0: 
        raise Http404()

    # создание переменной для передачи информации
    context = {
        'posts':posts,
        'cats': cats,
        'menu':menu,
        'title':'Отображение по рубрикам',
        'cat_selected': cat_id,
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
    cats = Category.objects.all()# обращение к классу Category и вывод всех экземпляров класса
    # Создание переменной context для передачи информации в html макет
    context = {
        'posts':posts,
        'cats': cats,
        'menu':menu,
        'title':'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'women/index.html', context=context)

def about(request): 
    return render(request, 'women/about.html', {'title': 'О сайте'})


# фунция для вывода ошибки page_not_found_404 (требует исправления)
def pageNotFound(request, exeption):
    return HttpResponseNotFound('<h1>КОД 404 Страница не найдена!</h1>')

