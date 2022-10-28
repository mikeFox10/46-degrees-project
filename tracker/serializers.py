from rest_framework import serializers

from .models import User, Iou

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user']

class IOUSerializer(serializers.ModelSerializer):
    amount = serializers.DecimalField(decimal_places=2, max_digits=30, min_value=0.01)
    class Meta:
        model = Iou
        fields = ['lender', 'borrower', 'expiration', 'amount']

class UserModel(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user']
    owes = serializers.DictField(
        child = serializers.CharField())
    owed_by = serializers.DictField(
        child = serializers.CharField())
    balance: serializers.DecimalField(decimal_places=2, max_digits=30)
