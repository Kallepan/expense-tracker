from rest_framework import serializers

from authentication.models import User

from .models import Payee, Expense

class PayeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payee
        fields = (
            "name",
        )

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = (
            "amount",
            "payee",
            "reason",

            "created_on",
            "created_by",
        )
        read_only_fields = (
            "created_on",
        )

    def to_representation(self, instance):
        repr = super().to_representation(instance)

        user_id = repr.pop("created_by", None)
        if user_id is None:
            repr["created_by"] = "Admin"
        else:
            repr["created_by"] = User.objects.get(id=user_id).username

        repr["created_on"] = str(repr["created_on"]).split("T")[0]
        return repr
