from django.shortcuts import render

# Create your views here.#csc
def index(request):
    return render(request, 'Desk/index.html')
def add_a_book(request):
    return render(request, 'Desk/add_a_book.html')