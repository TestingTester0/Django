from django.urls import path
from documents import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_document, name='upload_document'),
    path('test/', views.test, name='test'),
]