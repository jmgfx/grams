from django.shortcuts import render
from django.http import HttpResponse


def AssetView(render):
    return HttpResponse('Asset view goes here.')


def AssetTable(render):
    return HttpResponse('Asset table goes here.')
