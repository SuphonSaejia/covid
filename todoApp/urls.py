from django.urls import path
from todoApp import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('news',views.news,name='news'),


    path('delete/<itemID>',views.delete,name='delete'),
    path('Uncross/<itemID>',views.Uncross,name='Uncross'),
]