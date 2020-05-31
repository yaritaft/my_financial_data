import logging
from django.utils.timezone import datetime
from django.test import TestCase
from my_financial_app.models import (
    Account,
    Card,
    MoneyTransaction,
)



class TestModels(TestCase):
    def setUp(self):
        self.today = datetime.today()
