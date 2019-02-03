from django.shortcuts import render
from django.http import HttpResponse


def VendorsTable(render):
    return HttpResponse('This is the vendor table.')


def VendorsView(render):
    return HttpResponse('This is the vendor view.')
