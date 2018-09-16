"""sail_webpage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from sail_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('news/', views.news, name='news'),
    path('member/', views.member, name='member'),
    path('publications/', views.publications, name='publications'),
    path('course/', views.course, name='course'),
    path('students/', views.students, name='students'),
    path('opportunities/', views.opportunities, name='opportunities'),
    path('research1/', views.research1, name='research1'),
    path('research2/', views.research2, name='research2'),
    path('research3/', views.research3, name='research3'),
    path('research4/', views.research4, name='research4'),
    path('partner/', views.partner, name='partner')
]
