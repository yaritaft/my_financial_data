from enum import Enum

class CardType(Enum):
    MASTERCARD = 'MASTERCARD'
    VISA = 'VISA'
    AMEX = 'AMEX'

class TransactionType(Enum):
    CASHIN = 'CASHIN'
    CASHOUT = 'CASHOUT'

class TransactionCategory(Enum):
    LEISURE = 'LEISURE'
    FOOD = 'FOOD'
    INVESTMENT = 'INVESTMENT'
    SAVING = 'SAVING'
    SERVICES = 'SERVICES'
    RENT = 'RENT'
    GROCERIES = 'GROCERIES'
