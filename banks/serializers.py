from rest_framework import serializers
from .models import Banks, Branches


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banks
        fields = ['id', 'name', ]


class BranchSerializer(serializers.ModelSerializer):
    bank_name = serializers.ReadOnlyField(source='bank.name')
    bank_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Branches
        fields = ['ifsc', 'bank_id', 'bank_name', 'branch',
                  'address', 'city', 'district', 'state', ]
