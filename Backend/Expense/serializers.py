from rest_framework import serializers


class ExpenseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)
    amount = serializers.CharField()
    date = serializers.DateField()
    note = serializers.CharField()