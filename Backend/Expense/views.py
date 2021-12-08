from django.http import Http404


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Expense
from .serializers import (
    ExpenseSerializer,
    RegisterSerializer,
)
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.


# class ExpenseList(APIView):
#     serializer_classes  = (ExpenseSerializer)
#     def get(self, request, format=None):
#         expenses = Expense.objects.all()
#         serializer = ExpenseSerializer(expenses, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = ExpenseSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExpenseList(ListCreateAPIView):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()


    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class ExpenseDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
class RegisterView(APIView):
    def post(self, request, format=None):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetTotalExpense(APIView):
    def get(self, request, format=None):
        owner = request.user
        totalexpense = Expense.objects.filter(owner=owner)
        totalexpense=sum(totalexpense.values_list('amount', flat=True))
        return Response(totalexpense)