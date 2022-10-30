from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'listing/index.html')

@login_required(login_url='login')
def saved_page(request):
    return render(request, 'listing/saved.html')

def legals_page(request):
    return render(request, 'listing/legals.html')