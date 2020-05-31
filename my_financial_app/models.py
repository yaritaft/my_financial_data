from django.db import models
from django.utils.timezone import datetime

from my_financial_app.enums import CardType, TransactionType


class Account(models.Model):
    owner_name = models.CharField(max_length=200)
    owner_surname = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        """A string representation of the model."""
        return " ".join([self.owner_name, self.owner_surname])

class Card(models.Model):
    description = models.CharField(max_length=30)
    bank = models.CharField(max_length=40)
    card_type = models.CharField(
        max_length=200,
        choices=[(tag, tag.value) for tag in CardType]
    )
    owner = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        """A string representation of the model."""
        return self.description


class CashAccount(models.Model):
    owner = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        primary_key=True,
    )


class CashAccMonth(models.Model):
    beginning_calendar_date = models.DateTimeField(default=datetime.now)

class CardMonth(CashAccMonth):
    # If your new cycle begins on 22 o 23 you can set up that day
    # with beginning_calendar_date otherwise put first day of month
    closing_credit_card_date = models.DateTimeField(default=datetime.now)


class MoneyTransaction(models.Model):
    description = models.TextField(null=True)
    created_date = models.DateTimeField(default=datetime.now)
    amount = models.IntegerField()
    number_of_installments = models.IntegerField(null=True)
    total_number_of_installments = models.IntegerField(null=True)
    transaction_type = models.CharField(
        max_length=200,
        choices=[(tag, tag.value) for tag in TransactionType]
    )

    def __str__(self):
        """A string representation of the model."""
        return self.title