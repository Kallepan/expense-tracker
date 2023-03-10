from rest_framework import viewsets
from rest_framework import mixins

from .models import Expense, Payee
from .serializers import ExpenseSerializer, PayeeSerializer

class ExpenseViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet):

    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        qs = Expense.objects.all()
        user = self.request.user

        if user is None:
            return []

        return qs.filter(created_by=user.id)


class PayeeViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet):

    queryset = Payee.objects.all()
    serializer_class = PayeeSerializer