# dashboard, views.py
from datetime import timedelta
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils import timezone
from assets.models import Assets
from transactions.models import Transactions


def LogIn(request):
    return redirect('/login/')


@login_required
def Dashboard(request):
    time_limit = timezone.now().date() - timedelta(days=30)
    context = {
        'user': request.user,
        'asset_count': Assets.objects.filter(display=1).count(),
        'recently_added': Assets.objects.filter(date_added__gte=time_limit).count(),
        'queued_transactions': Transactions.objects.filter(status=1),
        'queued_transactions_count': Transactions.objects.filter(status=1).count(),
        'completed_transactions_count': Transactions.objects.filter(status=2).count(),
        'recent_actions': Transactions.objects.all(),
        'title': 'Home',
    }
    return render(request, 'dashboard.html', context)


def Notification(request):
    context = {
        'recent_actions': Transactions.objects.all(),
    }
    return render(request, 'notif.html', context)
