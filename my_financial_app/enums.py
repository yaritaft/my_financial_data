from enum import Enum

class CardType(Enum):
    MASTERCARD = 'MASTERCARD'
    VISA = 'VISA'
    AMEX = 'AMEX'

class TransactionType(Enum):
    CASHIN = 'CASHIN'
    CASHOUT = 'CASHOUT'