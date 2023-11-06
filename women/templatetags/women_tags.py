from django import template
from women.models import * 

# вывод повторяюзегося куска кода в теги и размещение их прямиком на html странице 

register = template.Library()

# регистрация происходит при помощи декоратора, 
# с возможностью изменния имени обращения, путем добавления атрибута "name"
# в остальном млучае обращение ведется по названию тега(функции) get_categories
@register.simple_tag(name='getcats')
def get_categories(filter=None):
    if not filter:
        return Category.objects.all() 
    else: 
        return Category.objects.filter(pk=filter)
# вклющающий тег отправляет кусок html кода 
# и в атрибуте вписывается путь к коду

@register.inclusion_tag('women/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    
    return {'cats':cats, 'cat_selected': cat_selected}



#########################################################
# вывод тега меню на страницу из
menu = [{'title':'О сайте', 'url_name':'about'},
        {'title':'Добавить статью', 'url_name':'addpage'},
        {'title':'Обратная связь', 'url_name':'contact'},
        {'title':'Войти', 'url_name':'login'},
] 

@register.inclusion_tag('women/menu_file.html')
def show_menu(): 
    return {'menu':menu}