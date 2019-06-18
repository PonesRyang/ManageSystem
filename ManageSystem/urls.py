"""ManageSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include

from window.views import login, get_index, sign, check_event, add_event

urlpatterns = [
    path('',get_index),
    path('login/', login),
    path('sign/', sign),
    path('port/', include('port.urls')),
    path('add_event/',add_event),
    path('check_event/', check_event),
    # path('deal_event/', ),
    # path('pass_event/', ),
    # path('leave/', ),
    # path('check_leave/', ),
    # path('pass_leave/', ),
    # path('user/', ),
    # path('scheduling/', )
]
