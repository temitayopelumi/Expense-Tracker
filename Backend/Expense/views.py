
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
  
from .models import Expense
from .serializers import ExpenseSerializer

# Create your views here.

class ExpenseList(APIView):

    def get(self, request, format=None):
        expenses = Expense.objects.all()
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)