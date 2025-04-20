"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/events/', views.show, name='list_events'),
    path('api/event/create', views.create_event, name='create_event'),
    path('api/event/update/<int:id>', views.update_event, name='update_event'),
    path('api/event/destroy/<int:id>', views.delete_event, name='delete_event'),
    path('api/track/<int:id>', views.create_track, name='create_track'),
    path('api/track/update/<int:id>', views.update_track, name='track_events'),
    path('api/track/delete/<int:id>', views.delete_track, name='delete_track'),
]
