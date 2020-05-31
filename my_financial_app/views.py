from rest_framework import generics, routers

from my_financial_app.serializers import (
    AccountSerializer,
    CardSerializer,
    MoneyTransactionSerializer,
)
from my_financial_app.models import (
    Account,
    Card,
    MoneyTransaction,
)

class ListAccountView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class DetailAccountView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class ListCardView(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class DetailCardView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class ListTransactionView(generics.ListCreateAPIView):
    queryset = MoneyTransaction.objects.all()
    serializer_class = MoneyTransactionSerializer

class DetailTransactionView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MoneyTransaction.objects.all()
    serializer_class = MoneyTransactionSerializer