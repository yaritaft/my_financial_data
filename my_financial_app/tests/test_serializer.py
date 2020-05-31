import logging
from django.utils.timezone import datetime
from django.test import TestCase
from my_financial_app.serializers import (
    AccountSerializer,
    # Card,
    # CardMonth,
    # CashAccMonth,
    # CashAccount,
    # MoneyTransaction,
)



class TestSer(TestCase):
    def setUp(self):
        self.today = datetime.today()

    def test_card_month(self):
        result = AccountSerializer(owner_name="yari", owner_surname="taft")
        assert result == {}