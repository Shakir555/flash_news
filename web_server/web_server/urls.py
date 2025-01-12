# Libraries
from django.contrib import admin
from django.urls import path, include

# URL Patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls')),
]

