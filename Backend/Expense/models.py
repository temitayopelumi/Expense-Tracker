from django.db import models


# Create your models here.
class Expense(models.Model):
    """Model definition for Expense."""

    # TODO: Define fields here
    CHOICES = (
        ("eatables", "Eatables"),
        ("drinks", "Drinks"),
        ("travel", "Travel"),
        ("housing", "Housing"),
        ("clothe", "Clothe"),
        ("books", "Book"),
        ("transport", "Transport"),
        ("grocery", "Grocery"),
        ("health", "Health"),
        ("security", "Security"),
        ("fun", "Fun"),
        ("repairs", "Repairs"),
        ("electronics", "Electronics"),
        ("fuel", "Fuel"),
        ("insurance", "Insurance"),
        ("others", "Others"),
    )

    name = models.CharField(max_length=50, choices=CHOICES)
    amount = models.CharField(max_length=50)
    date = models.DateField(auto_now=False, auto_now_add=False)
    note = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Expense."""

        verbose_name = "Expense"
        verbose_name_plural = "Expenses"

    def __str__(self):
        """Unicode representation of Expense."""
        return self.name
