from django.shortcuts import render
from django.http import HttpResponse


def start_page_view(request):
    return HttpResponse("hey das hat doch gut funktioniert!")