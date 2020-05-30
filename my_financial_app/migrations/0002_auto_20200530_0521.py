# Generated by Django 3.0.4 on 2020-05-30 05:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('my_financial_app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CardOwner',
        ),
        migrations.AlterField(
            model_name='account',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='cardmonth',
            name='closing_credit_card_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='cashaccmonth',
            name='beginning_calendar_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='moneytransaction',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]