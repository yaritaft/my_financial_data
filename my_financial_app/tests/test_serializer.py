import logging
from django.utils.timezone import datetime
from django.test import TestCase
from my_financial_app.serializers import (
    AccountSerializer,
)

class TestSer(TestCase):
    def setUp(self):
        pass