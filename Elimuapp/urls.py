
from django.contrib import admin
from django.urls import path
from Elimuapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('gallary/', views.gallary, name='gallary'),
    path('info/', views.information, name='info'),
    path('table/', views.table,name="table"),
    path('form/', views.form,name="form"),
    path('login/', views.login,name="login"),
    path('registration/', views.registration,name="registration"),

]
