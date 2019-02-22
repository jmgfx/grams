# dashboard, views.py
from datetime import timedelta
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from assets.models import Assets


def Dashboard(request):
    time_limit = timezone.now().date() - timedelta(days=30)
    context = {
        'asset_count': Assets.objects.all().count(),
        'recently_added': Assets.objects.filter(date_added__gte=time_limit).count(),
    }
    return render(request, 'dashboard.html', context, {'title': 'Dashboard'})