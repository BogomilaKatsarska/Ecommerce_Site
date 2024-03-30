from django.contrib import admin
from django.urls import path

from shop.views import index, detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('<int:id>/', detail, name='detail'),
]
