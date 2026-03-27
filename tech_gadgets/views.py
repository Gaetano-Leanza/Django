from django.shortcuts import render
from django.http import HttpResponse

from .dummy_data import gadgets, manufacturers

# Create your views here.

def start_page_view(request):
    return HttpResponse("Welcome to the Tech Gadgets page!")

def single_gadget_view(request):
    return HttpResponse(gadgets[0])