
from django.urls import path

from .views import ExpenseList,ExpenseDetail


app_name = "Expense"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('expense/',ExpenseList.as_view()),
    path('expense/<int:pk>/', ExpenseDetail.as_view())
]