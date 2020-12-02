from django.urls import path
from . import views


urlpatterns = [
    path('success/', views.ListCsvView.as_view(), name='success'),
    path("upload/", views.UploadCsvView.as_view(), name="upload"),
]