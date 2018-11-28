from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Receipt,Profile,House,Post
from .forms import NewProfileForm,NewReceiptForm


# Create your views here.

def welcome(request):

    return render(request,'welcome.html')


@login_required(login_url='/accounts/login/')
def home(request):
    posts=Post.objects.all()
    return render(request,'home.html',{"posts":posts})

@login_required(login_url='/accounts/login/')
def index(request):
    current_user=request.user

    receipts=Receipt.objects.all()
    # profile = Profile.objects.get(user_name=current_user)


    return render(request,'index.html',{"receipts":receipts,"profile":profile})

def profile(request):
    current_user=request.user
    receipts=Receipt.objects.filter(profile=current_user)

    if request.method == 'POST':
        form =NewProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.user_name = current_user
            profile.save()
        return redirect('profile')
    else:
        form=NewProfileForm()
    profile = Profile.objects.filter(user_name=current_user)

    if len(profile)<1:
        profile = "No profile"
    else:
        profile = Profile.objects.get(user_name=current_user)
    if request.method == 'POST':
        form =NewReceiptForm(request.POST,request.FILES)
        if form.is_valid():
            receipt=form.save(commit=False)
            receipt.profile = current_user
            receipt.save()
        return redirect('profile')
    else:
        form=NewReceiptForm()
    return render(request,'profile.html',{"profile":profile,"form":form,"receipts":receipts})

def create_profile(request):
    current_user=request.user
    if request.method == 'POST':
        form =NewProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.user_name = current_user
            profile.save()
        return redirect('profile')
    else:
        form=NewProfileForm()
    return render(request,'create_profile.html',{"form":form})

def new_receipt(request):
    current_user=request.user

    if request.method == 'POST':
        form =NewReceiptForm(request.POST,request.FILES)
        if form.is_valid():
            receipt=form.save(commit=False)
            receipt.profile = current_user
            receipt.save()
        return redirect('index')
    else:
        form=NewReceiptForm()
    return render(request,'receipt.html',{"form":form})

def vacant(request):
    houses=House.objects.filter(status="Vacant")
    return render(request,'houses.html',{"houses":houses})

def filter(request,house_id):
    receipts=Receipt.objects.filter(house_id=house_id)

    return render(request,'filter.html',{"receipts":receipts})
