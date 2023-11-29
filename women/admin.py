from django.contrib import admin

# Register your models here.
from .models import *

class WomenAdmin(admin.ModelAdmin): # Класс созданный для настрокий отображения в админ панеле 
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published') #  вывод полей 
    list_display_links = ('id', 'title') # Отмечает поля для создания ссылков для редактирования, сейчас можн отредактировать статью через название и id
    search_fields = ('title', 'content') # отвечает черзе какие поля будет  за поиск через админ панель
    list_editable = ('is_published',) # отвечает за редактирование через Админ панель
    list_filter = ('is_published', 'time_create') # отвечает за фильтрацию в Админ панеле
    prepopulated_fields = {'slug': ('title',)} #  автоматическое создание slug в админ панеле при создании поста

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name') # вывод полей
    list_display_link = ('id', 'name') # ссылки для редактирования из полей 
    search_fields = ('name',) # поиск исходя полей 
    prepopulated_fields = {'slug': ('name',)} # автоматическое создание slug изходя из названия

admin.site.register(Women, WomenAdmin)# Регистрация в админ панеле, сперва регистрируется модель, а следом класс с дополнительными настройками
admin.site.register(Category, CategoryAdmin)