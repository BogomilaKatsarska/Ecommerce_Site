from django.contrib import admin
from django.urls import path

from shop.views import index, detail, checkout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('<int:id>/', detail, name='detail'),
    path('checkout/', checkout, name='checkout'),
]
