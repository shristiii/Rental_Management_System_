from django.urls import path
from myproject import views

urlpatterns = [
    path('', views.home),
    path('dashboard/', views.index),
    path('login/', views.loginPage,name="loginPage"),
    path('register/', views.registerPage,name="registerPage"),
    path('bookPage/', views.bookPage,name="bookPage"),
    path('about/',views.about,name="about"),
    path('notify/', views.notify, name="notify"),
    path('forrent/',views.forrent,name="forrent"),
    path('book/<str:pk>',views.book,name="book"),
    path('submit/<str:pk>',views.submit,name="submit"),
    path('select/<str:pk>',views.select,name="select"),
    path('not_select/<str:pk>',views.not_select,name="not_select"),
    path('notify_submit',views.notify_submit,name="notify_submit"),
    path('notifyadmin/', views.notifyadmin, name="notifyadmin"),
    path('contact/', views.contact,name="contact"),
    path('detail/<str:pk>',views.detail,name="detail"),
    path('search', views.search, name='search'),
    path('read1', views.read1, name='read1'),
    path('read2', views.read2, name='read2'),
    path('read3', views.read3, name='read3'),
    path('read4', views.read4, name='read4'),
    path('read5', views.read5, name='read5'),
    path('read6', views.read6, name='read6'),
    path('read7', views.read7, name='read7'),
    path('read8', views.read8, name='read8'),
    path('room1', views.room1, name='room1'),
    path('room2', views.room2, name='room2'),
    path('room3', views.room3, name='room3'),
    path('room4', views.room4, name='room4'),
    path('room5', views.room5, name='room5'),
    path('room6', views.room6, name='room6'),
    path('room7', views.room7, name='room7'),
    path('room8', views.room8, name='room8'),



    

    

]