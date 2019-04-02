# dashboard, views.py
from datetime import timedelta
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils import timezone

from assets.models import Assets
from transactions.models import Transactions
from users.models import Permissions


@login_required
def Dashboard(request):
    time_limit = timezone.now().date() - timedelta(days=30)
    auth = Permissions.objects.get(user=request.user)

    if auth.branch is None:
        asset_count = Assets.objects.filter(display=1).count()
        recently_added = Assets.objects.filter(date_added__gte=time_limit).count()
        queued_transactions = Transactions.objects.filter(status=1)
        queued_transactions_count = Transactions.objects.filter(status=1).count()
        completed_transactions_count = Transactions.objects.filter(status=2).count()
        recent_actions = Transactions.objects.all()
    else:
        asset_count = Assets.objects.filter(branch=auth.branch).filter(display=1).count()
        recently_added = Assets.objects.filter(branch=auth.branch).filter(date_added__gte=time_limit).count()
        queued_transactions = Transactions.objects.filter(branch_origin=auth.branch).filter(status=1)
        queued_transactions_count = Transactions.objects.filter(branch_origin=auth.branch).filter(status=1).count()
        completed_transactions_count = Transactions.objects.filter(branch_origin=auth.branch).filter(status=2).count()
        recent_actions = Transactions.objects.filter(branch_origin=auth.branch).all()

    context = {
        'user': request.user,
        'asset_count': asset_count,
        'recently_added': recently_added,
        'queued_transactions': queued_transactions,
        'queued_transactions_count': queued_transactions_count,
        'completed_transactions_count': completed_transactions_count,
        'recent_actions': recent_actions,
        'title': 'Home',
    }
    return render(request, 'dashboard.html', context)
