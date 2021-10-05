from rest_framework import serializers
from .models import Expense

class ExpenseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)
    amount = serializers.CharField()
    date = serializers.DateField()
    note = serializers.CharField()

    class Meta:
        model = Expense
        fields = ('__all__')


    def create(self,validated_data): 
        return Expense.objects.create(**validated_data)


    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.date = validated_data.get('date', instance.date)
        instance.note = validated_data.get('note', instance.note)
        instance.save()
        return instance