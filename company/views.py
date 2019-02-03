from django.shortcuts import render
from django.http import HttpResponse


def CompanyView(render):
    return HttpResponse('Company view goes here.')


def CompanyTable(render):
    return HttpResponse('Company table goes here.')
