from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Receipt,Profile,House


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    receipts=Receipt.objects.all()

    return render(request,'index.html',{"receipts":receipts})
