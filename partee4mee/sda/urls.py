"""sda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from partee.views import main, add, your_account, party_signed_up_by_user, user_signed_up_events, edit_event

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', main, name="main"),
    path('add_party/', add, name="add_event"),
    path('your_account/', your_account, name="your_account"),
    path('signed_up_events/<int:pk>', party_signed_up_by_user, name="party_signed_up_by_user"),
    path('user_signed_up_events/', user_signed_up_events, name="user_signed_up_events"),
    path('edit_event/<int:id>/', edit_event, name="edit"),
    path('accounts/', include('accounts.urls')),
]

