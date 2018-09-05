from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('',include(my_blog.urls)),
    path('admin/', admin.site.urls),
]
