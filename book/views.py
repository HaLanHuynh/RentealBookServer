from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import GetAllBooksSerializer


class GetAllBooksAPIView(APIView):
    def get(self, request):
        list_book = Book.objects.all()
        mydata = GetAllBooksSerializer(list_book, many=True)
        return Response(data=mydata.data, status=status.HTTP_200_OK)

# Create your views here.
