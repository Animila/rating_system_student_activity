from django.contrib import admin
from django.urls import path, include
from cabinet import views
import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cabinet/', views.cabinet, name="cabinet"),
    path('', include('home.urls')),
]
