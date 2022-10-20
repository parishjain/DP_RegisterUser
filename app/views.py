from email import message
from typing import Container
from django.shortcuts import render
from . models import *
# Create your views here.

def SignUpPage(request):
    return render(request,"app/signup.html")

def SignUpRequest(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        contact = request.POST['contact']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        user = UserData.objects.filter(Email=email)

        if user:
            message = "User already exist"
            return render(request,"app/signup.html",{'msg':message})
        else:
            if password == cpassword:
                newuser = UserData.objects.create(Firstname=fname,Lastname=lname,Email=email,Contact=contact,Password=password)
                message = "User Registered Successfully"
                return render(request,"app/login.html",{'msg':message})
            else:
                message="Password and Confirm Password Does not Match"
                return render(request,"app/signup.html",{'msg':message})


def Loginpage(request):
    return render(request,"app/login.html")


def Loginuser(request):
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']

        #checking email with Database
        try:
            user = UserData.objects.get(Email = email)
            # print(user)
        except UserData.DoesNotExist:
            user = None

        if user:
            if user.Password == password:
                request.session['Firstname'] = user.Firstname
                request.session['Lastname'] = user.Lastname
                request.session['Emailid'] = user.Email
                request.session['Contact'] = user.Contact
                return render(request,"app/home.html")
            else:
                message = "Password does not match"
                return render(request,"app/signup.html",{'msg':message})
        else:
            message = "User does not exist"
            return render(request,"app/signup.html",{'msg':message})

def Homepage(request):
    return render(request,"app/home.html")


def Contactus(request):
    if request.method=='POST':
        firstname = request.session['Firstname']
        email = request.session['Emailid']
        contact = request.POST['contact']
        message = request.POST['message']
        contactuser = ContactForm.objects.create(Name = firstname,Email=email,Contact=contact,Message=message)
        message = "Message Sended successfully"
        return render(request,"app/home.html",{'msg':message})
