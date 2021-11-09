from django.urls import path, include

from .views import ExpenseList, ExpenseDetail


app_name = "Expense"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path("expense/", ExpenseList.as_view()),
    path("expense/<int:pk>/", ExpenseDetail.as_view()),
    path("auth/", include("rest_auth.urls")),
    path("users/", include("users.urls")),
]
