from django.db import models
from django.utils.timezone import now

from .enums import CardType, TransactionType


class Account(models.Model):
    owner_name = models.CharField(max_length=200)
    owner_surname = models.CharField(max_length=200)
    created_date = models.DateField(default=now)

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
    owner = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        """A string representation of the model."""
        return self.title


class CashAccount(models.Model):
    owner = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        primary_key=True,
    )


class CashAccMonth(models.Model):
    beginning_calendar_date = models.DateField(default=now)

class CardMonth(CashAccMonth):
    # If your new cycle begins on 22 o 23 you can set up that day
    # with beginning_calendar_date otherwise put first day of month
    closing_credit_card_date = models.DateField(default=now)


class MoneyTransaction(models.Model):
    description = models.TextField(null=True)
    created_date = models.DateField(default=now)
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