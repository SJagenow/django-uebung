from django.shortcuts import render
from django.http import HttpResponse
from dummy_data import gadgets

def start_page_view(request):
    return HttpResponse("hey das hat doch gut funktioniert!")

def single_gadget_view(request):
    return HttpResponse(gadgets[0])