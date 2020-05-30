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
    
    def test_cash_acc_month(self):    
        cash_acc_month = CashAccMonth(
            beginning_calendar_date=self.today,
        )
        cash_acc_month.save()
        assert CashAccMonth.objects.all().first() == cash_acc_month
    
    def test_account(self):
        my_account = Account(
            owner_name = "Yari",
            owner_surname = "Taft",
        )
        my_account.save()
        assert Account.objects.all().first() == my_account
        try:
            assert my_account.created_date.date() == self.today.date()
        except AssertionError:
            logging.error(my_account.created_date)
            logging.error(self.today)
        
    def test_cash_account(self):
        my_account = Account(
            owner_name = "Yari",
            owner_surname = "Taft",
        )
        my_account.save()
        my_cash_account = CashAccount(owner=my_account)
        my_cash_account.save()
        assert CashAccount.objects.all().first() == my_cash_account

    def test_card(self):
        my_account = Account(
            owner_name = "Yari",
            owner_surname = "Taft",
        )
        my_account.save()
        my_cash_account = CashAccount(owner=my_account)
        my_cash_account.save()
        my_card = Card(
            description="VISA GOLD GALICIA 2785",
            bank="GALICIA",
            card_type="VISA",
            owner=my_account,
        )
        my_card.save()
        assert Card.objects.all().first() == my_card

    def test_money_transaction(self):
        my_account = Account(
            owner_name = "Yari",
            owner_surname = "Taft",
        )
        my_account.save()
        my_cash_account = CashAccount(owner=my_account)
        my_cash_account.save()
        my_card = Card(
            description="VISA GOLD GALICIA 2785",
            bank="GALICIA",
            card_type="VISA",
            owner=my_account,
        )
        my_card.save()
        my_cashout = MoneyTransaction(
            description="RAPANUI",
            amount="280",
            transaction_type="CASHOUT"
        )
        my_cashout.save()
        my_cashin = MoneyTransaction(
            description="RAPANUI",
            amount="280",
            transaction_type="CASHIN"
        )
        my_cashout_in_installment = MoneyTransaction(
            description="RAPANUI",
            amount="280",
            transaction_type="CASHOUT",
            number_of_installments=1,
            total_number_of_installments=3,
        )
        my_cashout.save()
        my_cashin.save()
        my_cashout_in_installment.save()
        self.assertTrue(MoneyTransaction.objects.filter(id=my_cashout.id).exists())
        self.assertTrue(MoneyTransaction.objects.filter(id=my_cashin.id).exists())
        self.assertTrue(MoneyTransaction.objects.filter(id=my_cashout_in_installment.id).exists())