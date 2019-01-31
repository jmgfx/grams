from django.shortcuts import render
from django.http import HttpResponse


def BranchTable(render):
    return HttpResponse('This is the branch table.')


def BranchView(render):
    return HttpResponse('This is the branch view.')