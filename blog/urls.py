from django.urls import path
from . import views

urlpatterns = [
    path('',views.blogHome,name='blogHome'),   # this corresponds project me se .../blog pe aa rha hai toh ider aa jaye isme blog ka home function return ho 
    path('postComment',views.postComment,name='postComment'),  # this should be written before slug kyuki nhi to slug me chla jyga ye bi
    path('<str:slug>/',views.blogPost , name='blogPost')
]