from django.db import models

from my_financial_app.enums import (
    CardType,
    TransactionCategory,
    TransactionType,
)


class Account(models.Model):
    owner_name = models.CharField(max_length=200)
    owner_surname = models.CharField(max_length=200)
    created_date = models.DateField(auto_now_add=True)

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

class MoneyTransaction(models.Model):
    # Some transactions will be automatically created by installments
    description = models.CharField(
        max_length=200,
    )
    created_date = models.DateField(auto_now_add=True)
    category = models.CharField(
        max_length=200,
        choices=[(tag, tag.value) for tag in TransactionCategory]
    )
    amount = models.IntegerField()
    number_of_installments = models.IntegerField(default=1)
    total_number_of_installments = models.IntegerField(default=1)
    transaction_type = models.CharField(
        max_length=200,
        choices=[(tag, tag.value) for tag in TransactionType]
    )
    card = models.ForeignKey(
        Card,
        on_delete=models.CASCADE
    )

    def __str__(self):
        """A string representation of the model."""
        return self.description