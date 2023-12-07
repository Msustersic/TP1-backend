"""
URL configuration for ias project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from .views import IasPage
from .views import ByFunctionPage
from .views import CommentsPage
from .views import LoginForm
from .views import logout_view
from .views import CommentsForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IasPage.as_view(), name= 'inicio'),
    path('byFunction/', ByFunctionPage.as_view(), name= 'byFunction'),
    path('comments/', CommentsPage.as_view(), name= 'comments'),
    path('fComments/', CommentsForm.as_view(), name= 'fComments'),
    path('logout/', logout_view, name='logout'),
    path('login/', LoginForm.as_view(), name= 'fLogin'),
]

