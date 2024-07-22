from django.urls import path
from .views import category,contact,index,single,base

urlpatterns = [
    path('',index,name = "index"),
    path('contact',contact,name = "contact"),
    path('category',category, name = 'category'),
    path('single /<int:id>',single,name = 'single'),
    path('base',base ,name = "base")
]





