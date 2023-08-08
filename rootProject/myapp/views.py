from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import *
# Create your views here.
# define variable of all models:
A_home_slide_data= A_home_slide.objects.all()
B_about_data = B_about.objects.all()
C_course_data =  C_course.objects.all()
D_advisor_data = D_advisor.objects.all()
E_events_data = E_events.objects.all()
F_news_data = F_news.objects.all()
G_shop_data = G_shop.objects.all()
H_subscriber_data = H_subscriber.objects.all()
I_question_data = I_question.objects.all()

context = {
        'home_data': A_home_slide_data,
        'about_data': B_about_data,
        'course_data': C_course_data,
        'advisor_data': D_advisor_data,
        'events_data' : E_events_data,
        'news_data': F_news_data,
        'shop_data': G_shop_data
    } 

def login_user(request):
    if request.method == "POST":
        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)

        if user is not None:
            
            login(request,user)
            return redirect('index')
        else:
            messages.error(request,"incorrect username or password!!")
            return redirect('login') 
        
    return render(request,'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('login')    
    

def register_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.warning(request,"This username already exist!")
                return redirect('signup')
            else: 
                user = User.objects.create_user(username=username,password=password)
                user.save()
                messages.warning(request,"successfully registered!")
                return redirect('login')
        else:
             messages.warning(request,"This Password Does Not Matched!")        
                 
    return render(request,"signup.html")


def index(request):
    
    if request.method == "POST":
        email = request.POST.get('email')
        
        H_subscriber_mail = H_subscriber(
            email = email
        )
        H_subscriber_mail.save()
        return redirect('index')
    
    return render(request, 'index.html',context)


def events(request):
    if request.method == "POST":
        email = request.POST.get('email')
        
        H_subscriber_mail = H_subscriber(
            email = email
        )
        H_subscriber_mail.save()
        return redirect('events')
    return render(request, 'events_01.html',context={'events_data':E_events_data})


def events_2(request):
    if request.method == "POST":
        email = request.POST.get('email')
        
        H_subscriber_mail = H_subscriber(
            email = email
        )
        H_subscriber_mail.save()
        return redirect('events_2')
    return render(request, 'events_02.html')


def events_details(request):
    if request.method == "POST":
        email = request.POST.get('email')
        
        H_subscriber_mail = H_subscriber(
            email = email
        )
        H_subscriber_mail.save()
        return redirect('events_details')
    return render(request, 'event_details.html')


def course(request):
    if request.method == "POST":
        email = request.POST.get('email')
        
        H_subscriber_mail = H_subscriber(
            email = email
        )
        H_subscriber_mail.save()
        return redirect('course')
    return render(request, 'course_01.html',context={'course_data': C_course_data})


def course_details(request):
    if request.method == "POST":
        email = request.POST.get('email')
        
        H_subscriber_mail = H_subscriber(
            email = email
        )
        H_subscriber_mail.save()
        return redirect('course_details')
    return render(request, 'course_details.html')


def news(request):
    if request.method == "POST":
        email = request.POST.get('email')
        
        H_subscriber_mail = H_subscriber(
            email = email
        )
        H_subscriber_mail.save()
        return redirect('news')
    return render(request, 'grid_news.html',context={'news_data': F_news_data})


def news_details(request):
    if request.method == "POST":
        email = request.POST.get('email')
        
        H_subscriber_mail = H_subscriber(
            email = email
        )
        H_subscriber_mail.save()
        return redirect('news_details')
    return render(request, 'news_details.html')


def shop(request):
    if request.method == "POST":
        email = request.POST.get('email')
        
        H_subscriber_mail = H_subscriber(
            email = email
        )
        H_subscriber_mail.save()
        return redirect('shop')
    return render(request, 'shop_pages.html',context={'shop_data': G_shop_data})


def contact(request):
    if request.method == "POST":
        if request.POST.get('name'):
            question = I_question(
                name = request.POST.get('name'),
                email = request.POST.get('email'),
                subject = request.POST.get('subject'),
                experience = request.POST.get('exp'),
                message = request.POST.get('message')
            )
            question.save()
            return redirect('contact')
    
    
    if request.method == "POST":
        email = request.POST['email']
        
        H_subscriber_mail = H_subscriber(
            email = email
        )
        H_subscriber_mail.save()
        return redirect('contact')
    return render(request, 'contact_us.html')