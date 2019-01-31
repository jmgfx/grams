from django.shortcuts import render
from django.http import HttpResponse


def TransactionsView(render):
    return HttpResponse('Transactions view goes here.')


def TransactionsTable(render):
    return HttpResponse('Transactions table goes here.')
