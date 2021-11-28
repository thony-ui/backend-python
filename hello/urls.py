from django.urls import path
from hello import views

urlpatterns = [
    path("", views.home, name="home"),
    path("counter", views.counter, name="counter"),
    path('portfolio', views.portfolio, name = 'portfolio'),
    path('index3', views.home2, name='home2'),
    path('register', views.register, name='register'),
    path('login', views.login, name = 'login'),
    path('logout', views.logout,name='logout'),
    path('post/<str:pk>', views.post, name='post')
]

#when the path(''), it means it is the root/original url