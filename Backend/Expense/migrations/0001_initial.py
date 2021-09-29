# Generated by Django 3.2.6 on 2021-09-28 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('eatables', 'Eatables'), ('drinks', 'Drinks'), ('travel', 'Travel'), ('housing', 'Housing'), ('clothe', 'Clothe'), ('books', 'Book'), ('transport', 'Transport'), ('grocery', 'Grocery'), ('health', 'Health'), ('security', 'Security'), ('fun', 'Fun'), ('repairs', 'Repairs'), ('electronics', 'Electronics'), ('fuel', 'Fuel'), ('insurance', 'Insurance'), ('others', 'Others')], max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('date', models.DateTimeField(auto_now=True)),
                ('note', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Expense',
                'verbose_name_plural': 'Expenses',
            },
        ),
    ]