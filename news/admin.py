from django.contrib import admin
from .models import Category, News
# Register your models here.



class NewsAdmin(admin.ModelAdmin):
    list_display=["title",'description','category']

admin.site.register(Category)
admin.site.register(News,NewsAdmin)