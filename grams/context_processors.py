from django.contrib.auth.models import User
from transactions.models import Transactions
from users.models import Permissions
from django.contrib.auth.decorators import login_required


def Notifications(request):
    if not request.user.is_authenticated:
        return {
            'notifications': Transactions.objects.filter(status=1)
        }
    elif request.user.is_anonymous:
        return {
            'notifications': Transactions.objects.filter(status=1)
        }

    try:
        auth = Permissions.objects.get(user=request.user)
        if auth.branch is None:
            return {
                'notifications': Transactions.objects.filter(status=1)
            }
        else:
            branch_auth = auth.branch
            return {
                'notifications': Transactions.objects.filter(branch_origin=branch_auth).filter(status=1)
            }
    except Permissions.DoesNotExist:
        return {
            'notifications': Transactions.objects.filter(status=1)
        }


def PermissionsAuth(request):
    if not request.user.is_authenticated:
        return {
            'soft_auth': 'General User',
        }
    
    try:
        return {
            'soft_auth': Permissions.objects.get(user=request.user).permission,
        }
    except Permissions.DoesNotExist:
        return {
            'soft_auth': 'General User',
        }