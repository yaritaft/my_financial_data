from django.utils.timezone import datetime
from rest_framework import serializers
from my_financial_app.enums import CardType, TransactionType
from my_financial_app.models import (
    Account,
    Card,
    CardMonth,
    CashAccMonth,
    CashAccount,
    MoneyTransaction,
)

class AccountSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    owner_name = serializers.CharField(
        required=True, allow_blank=True, max_length=100
    )
    owner_surname = serializers.CharField(
        required=True, allow_blank=True, max_length=100
    )
    created_date = serializers.DateTimeField(
        required=False,
    )
    card_set = serializers.HyperlinkedRelatedField(many=True, view_name='card-detail', read_only=True)

    class Meta:
        fields = ["id", "owner_name", "owner_surname", "created_date", "card_set"]
        model = Account

class CardSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    description = serializers.CharField(max_length=30)
    bank = serializers.CharField(max_length=40)
    card_type = serializers.CharField(
        max_length=200
    )
    owner = serializers.IntegerField(write_only=True)
    class Meta:
        fields = ["id", "description", "bank", "card_type", "owner"]
        model = Account
    
    def create(self, validated_data):
        account_id = validated_data["owner"]
        account = Account.objects.get(id=account_id)
        validated_data["owner"] = account
        card = Card.objects.create(**validated_data)
        return card
