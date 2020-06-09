from django.utils.timezone import datetime
from rest_framework import serializers
from my_financial_app.enums import CardType, TransactionType
from my_financial_app.models import (
    Account,
    Card,
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
    created_date = serializers.DateField(
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

class MoneyTransactionSerializer(serializers.HyperlinkedModelSerializer):
    description = serializers.CharField()
    created_date = serializers.DateField(
        required=False,
    )
    category = serializers.CharField(
        max_length=200
    )
    amount = serializers.IntegerField()
    number_of_installments = serializers.IntegerField(required=False)
    total_number_of_installments = serializers.IntegerField(required=False)
    transaction_type = serializers.CharField(
        max_length=200
    )
    card_id = serializers.IntegerField(write_only=True)
    class Meta:
        fields = [
            "id",
            "description",
            "created_date",
            "category",
            "amount",
            "number_of_installments",
            "total_number_of_installments",
            "transaction_type",
            "card_id"
        ]
        model = MoneyTransaction
    
    def create(self, validated_data):
        my_card_id = validated_data["card_id"]
        my_card = Card.objects.get(id=my_card_id)
        validated_data["card"] = my_card
        money_transaction = MoneyTransaction.objects.create(**validated_data)
        return money_transaction
