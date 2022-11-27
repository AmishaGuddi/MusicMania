from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('english/', views.index_english, name = "homeenglish"),
    path('hindi/', views.index_hindi, name = "homehindi"),
    path('asklang/', views.ask_lang, name = "ask_lang"),
    path('korean/', views.index_korean, name = "homekorean"),
    path('login/', views.handle_login, name = "login"),
    path('logout/', views.do_logout, name = "logout"),
    path('signup/', views.signup, name = "signup"),
]
