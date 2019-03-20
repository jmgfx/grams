from django.contrib.auth.models import User
from transactions.models import Transactions

def Notifications(request):
    return {
        'notifications': Transactions.objects.filter(status=1),
    }