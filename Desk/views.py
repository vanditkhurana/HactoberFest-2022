from django.shortcuts import render
from django.views import Views
from django.views.generic import TemplateView
# Create your views here.#csc
def index(request):
    return render(request, 'Desk/index.html')
def add_a_book(request):
    return render(request, 'Desk/add_a_book.html')


def aboutus(request):
    return render(request, 'Desk/about_us.html')
    
