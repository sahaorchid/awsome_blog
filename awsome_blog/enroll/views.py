from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from .forms import signupForm,loginForm,addpostform
from django.contrib import messages
from .models import post

#about page
def about(request):
    return render(request,'enroll/about.html')
#updatepost page
def updatepost(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=post.objects.get(pk=id)
            form=addpostform(request.POST,instance=pi)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/dashboard/')
        else:
            pi=post.objects.get(pk=id)
            form=addpostform(instance=pi)
    else:
        return HttpResponseRedirect('/login/')
    return render(request,'enroll/updatepost.html',{'form':form})
def deletepost(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi = post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')

#addpost page
def addpost(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=addpostform(request.POST)
            if fm.is_valid():
                titel=fm.cleaned_data['titel']
                desc=fm.cleaned_data['desc']
                username=request.user.username
                pst=post(titel=titel,desc=desc,username=username)
                pst.save()
                form=addpostform()
        else:
            form=addpostform()
    return render(request,'enroll/addpost.html',{'form':form})

#contact page
def contact(request):
    return render(request,'enroll/contact.html')
def sign_up(request):
        if request.method=="POST":
            fm=signupForm(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,'Congratulations!! Signup successfully')
                return HttpResponseRedirect('/login/')
        else:
            fm=signupForm()
        return render(request,'enroll/signup.html',{'form':fm})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            af=loginForm(request=request,data=request.POST)
            if af.is_valid():
                uname=af.cleaned_data['username']
                upass = af.cleaned_data['password']
                user=authenticate(request,username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request, 'Login successfully!!')
                    return HttpResponseRedirect('/')
        else:
            af=loginForm()

        return render(request,'enroll/login.html',{'login':af})
    else:
        return HttpResponseRedirect('/dashboard/')


def user_profile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    else:
        user_data=post.objects.filter(username=request.user.username)
        return render(request,'enroll/dashboard.html',{'userdata':user_data})

def user_logout(request):
        logout(request)
        return HttpResponseRedirect('/')

#home page
def home(request):
    posts=post.objects.all()
    return render(request,'enroll/home.html',{'posts':posts})

