# Generated by Django 5.0.6 on 2024-08-07 10:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_alter_expense_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expense',
            options={'ordering': ('-date', '-pk')},
        ),
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='expense_category', to='expenses.category'),
        ),
    ]
