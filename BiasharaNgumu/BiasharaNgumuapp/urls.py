from django.contrib import admin
from django.urls import path

from BiasharaNgumuapp import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.home)

]
