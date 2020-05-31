import logging
from django.utils.timezone import datetime
from django.test import TestCase
from my_financial_app.models import (
    Account,
    Card,
    CardMonth,
    CashAccMonth,
    CashAccount,
    MoneyTransaction,
)



class TestModels(TestCase):
    def setUp(self):
        self.today = datetime.today()

    def test_card_month(self):
        card_month = CardMonth(
            closing_credit_card_date=self.today,
            beginning_calendar_date=self.today,
        )
        card_month.save()
        assert CardMonth.objects.all().first() == card_month