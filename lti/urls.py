"""lti URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
<<<<<<< HEAD
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
=======
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
>>>>>>> 9c0d89f19846b2c71a2805b88b574c98dcdd220a
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import django_app_lti.urls
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^lti/', include(django_app_lti.urls, namespace="lti")),
    url(r'^lti-test/$', views.MyLTILaunchView.as_view(), name='lti-test')

]
