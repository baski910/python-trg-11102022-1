from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

# Create your views here.

class BookViews(APIView):
    def get(self,request,id=None):
        if id:
            book = Book.objects.get(id=id)
            serializer = BookSerializer(book)
            return Response(
                {
                    "status": "success",
                    "data": serializer.data
                },
                status = status.HTTP_200_OK
            )
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(
                {
                    "status": "success",
                    "data": serializer.data
                },
                status = status.HTTP_200_OK
            )
    
    def post(self,request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": "success",
                    "data": request.data
                },
                status = status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    "status": "error",
                    "data": serializer.errors
                },
                status = status.HTTP_400_BAD_REQUEST
            )


