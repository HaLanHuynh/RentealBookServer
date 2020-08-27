from .views import GetAllBooksAPIView
from django.urls import path

urlpatterns = [
    path('books/', GetAllBooksAPIView.as_view()),
]