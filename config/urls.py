"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app.views import rounded, letters, pet, long_sum
urlpatterns = [
    path("warmup1/near-hundred/<number1>", rounded),
    path("warmup2/String-Splosion/<str:letters>", letters),
    path("string2/cat-dog/<pet>",pet),
    path("Logic2/lone-sum/<a>/<b>/<c>",long_sum),
    path('admin/', admin.site.urls),
]
