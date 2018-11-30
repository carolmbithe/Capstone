from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Receipt,Profile,House,Post,Request
from .forms import NewProfileForm,NewReceiptForm,NewPostForm,NewRequestForm


# Create your views here.

def welcome(request):

    return render(request,'welcome.html')


@login_required(login_url='/accounts/login/')
def home(request):
    posts=Post.objects.all()
    if request.method == 'POST':
        form =NewPostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.name = current_user
            post.save()
        return redirect('home')
    else:
        form=NewPostForm()
    return render(request,'home.html',{"posts":posts,"form":form})

@login_required(login_url='/accounts/login/')
def request(request):

    return render(request,'home.html',{"posts":posts,"form":form})

@login_required(login_url='/accounts/login/')
def index(request):
    current_user=request.user

    receipts=Receipt.objects.all()
    requests=Request.objects.all()

    # profile = Profile.objects.get(user_name=current_user)


    return render(request,'index.html',{"receipts":receipts,"profile":profile,"requests":requests})

def profile(request):
    current_user=request.user
    receipts=Receipt.objects.filter(profile=current_user)

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

def edit_profile(request):
   current_user = request.user
   if request.method == 'POST':
       instance = Profile.objects.get(user_name=current_user)
       form = NewProfileForm(request.POST, request.FILES,instance=instance)
       if form.is_valid():
           profile = form.save(commit = False)
           profile.user = current_user
           profile.save()

       return redirect('profile')
   elif Profile.objects.get(user_name=current_user):
       profile = Profile.objects.get(user_name=current_user)
       form = NewProfileForm(instance=profile)
   else:
       form = NewProfileForm()
   return render(request,'edit_profile.html',{'form':form})

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

def new_post(request):
    current_user=request.user

    if request.method == 'POST':
        form =NewPostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.name = current_user
            post.save()
        return redirect('home')
    else:
        form=NewPostForm()
    return render(request,'post.html',{"form":form})

def vacant(request):
    houses=House.objects.filter(status="Vacant")
    requests=Request.objects.all()
    if request.method == 'POST':
        form =NewRequestForm(request.POST,request.FILES)
        if form.is_valid():
            request=form.save(commit=False)
            request.save()
        return redirect('vacant')
    else:
        form=NewRequestForm()
    return render(request,'houses.html',{"houses":houses,"requests":requests,"form":form})

def house(request,house_id):
    receipts=Receipt.objects.filter(room_number_id=house_id)

    return render(request,'house.html',{"receipts":receipts})
