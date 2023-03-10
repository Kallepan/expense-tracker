from rest_framework import routers

from .views import PayeeViewSet, ExpenseViewSet

router = routers.SimpleRouter()

router.register(r'payees', PayeeViewSet)
router.register(r'expenses', ExpenseViewSet)

urlpatterns = [

] + router.urls