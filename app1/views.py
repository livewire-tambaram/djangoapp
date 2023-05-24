from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from app1.forms import EnquiryForm
from app1.models import Enquiry

# Create your views here.
def homePage(request):
    return render(request,'home.html')

def aboutPage(request):
    ctime = datetime.now()
    return render(request,'about.html',{"time":ctime,'student1':"SHANKAR r","student2":"raam"})

def coursePage(request):
    return render(request,'courses.html')

def enquiryPage(request):
    fm = EnquiryForm(request.POST or None)
    if fm.is_valid():
        fm.save()
        return HttpResponse("Your Form Submitted successfully")
    return render(request,'enquiry.html',{'data':fm})

@login_required(login_url='/login')
def viewEnquiry(request):
    data = Enquiry.objects.all()
    return render(request,'enquiries.html',{'enq':data})
@login_required(login_url='/login')
def updateEnquiry(request,id):
    obj = get_object_or_404(Enquiry,pk=id)
    form = EnquiryForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponse("Updated Successfully!")
    return render(request,'updateEnquiry.html',{'form':form})
@login_required(login_url='/login')
def deleteEnquiry(request,id):
    obj = get_object_or_404(Enquiry,pk=id)
    if request.method=="POST":
        obj.delete()
        return HttpResponse('Deleted Successfully!')
    return render(request,'deleteEnq.html',{"data":obj})

def signupPage(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'signup.html',{'myform':form})

def staffPage(request):
    return render(request,'staffpage.html')