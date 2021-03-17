from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from .forms import ServiceForm,DemandForm,ServiceUForm,DemandUForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Service,Demand,Brand,Agent

# Create your views here.

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def machines(request):
    return render(request,"machines.html")

def consumables(request):
    return render(request,"consumables.html")

def home(request):
    return render(request,"home.html")

def success(request):
    return render(request,"success.html")

def test(request):
    return render(request,"test.html")

def logined(request):
    return render(request,"logined.html")

def products(request):
    return render(request,"products.html")

            #FORMS

def service(request):
    form = ServiceForm(request.POST or None)
    context = {
        "form" : form,
        
    }
    


    if form.is_valid():
        form.save()
        subject = "Yeni Servis Talebi Oluşturuldu!  --->  "+ str(form.cleaned_data["name"])
        body = {
            "title" : str("Formu Oluşturanın Bilgileri:"),
            'name' : "İsim: "+str(form.cleaned_data["name"]),
            'company_name' : "Firma: "+str(form.cleaned_data["company_name"]),
            'phone' : "Telefon Numarası: "+ str(form.cleaned_data['phone']),
            'mail' : "E-Mail: "+str(form.cleaned_data['mail']),
            'brand' : "Marka: "+str(form.cleaned_data['brand']),
            'submodel' : "Model: "+str(form.cleaned_data['submodel']),
            'content' : "Detay:\n      "+str(form.cleaned_data['content']),
        }

        message = "\n".join(body.values())
        
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            ["mehmetemin@tastaban.net"],
            fail_silently=False
        )
        return redirect("success")
    return render(request,"service.html",context)

def demand(request):
    form = DemandForm(request.POST or None)
    context = {
        "form" : form,
        
    }
    


    if form.is_valid():
        form.save()
        subject = "Yeni Teklif Talebi Oluşturuldu  --->  "+ str(form.cleaned_data["name"])
        body = {
            "title" : str("Formu Oluşturanın Bilgileri:"),
            'name' : "İsim: "+str(form.cleaned_data["name"]),
            'company_name' : "Firma: "+str(form.cleaned_data["company_name"]),
            'phone' : "Telefon Numarası: "+ str(form.cleaned_data['phone']),
            'mail' : "E-Mail: "+str(form.cleaned_data['mail']),
            'product' : "Talep Edilen Ürün: "+str(form.cleaned_data['product']),
            'quantity' : "Talep Edilen Miktar: "+str(form.cleaned_data['quantity']),
            'content' : "Detay:\n      "+str(form.cleaned_data['content']),
        }

        message = "\n".join(body.values())
          
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            ["mehmetemin@tastaban.net"],
            fail_silently=False
        )
        return redirect("success")
    return render(request,"productdemand.html",context)

            #DASHBOARD

def dashboard(request):
    
    if request.user.is_authenticated:
        services = Service.objects.filter( agent = 17)
        pdemands = Demand.objects.filter( agent = 17 )
        context = {
            "services" : services,
            "pdemands" : pdemands
        }

        return render(request,"dashboard.html",context)
    else:
        return redirect("/user/login")
def dashservices(request):
    if request.user.is_superuser:
        services = Service.objects.filter()
        context = {
            "services" : services
        }

        return render(request,"dashservices.html",context)
    elif request.user.is_authenticated:
        services = Service.objects.filter(agent = request.user)
        context = {
            "services" : services
        }

        return render(request,"dashservices.html",context)
    else:
        return redirect("/user/login")

def dashpd(request):
    if request.user.is_superuser:
        pdemands = Demand.objects.filter()
        context = {
            "pdemands" : pdemands
        }

        return render(request,"dashpd.html",context)
    elif request.user.is_authenticated:
        pdemands = Demand.objects.filter(agent=request.user)
        context = {
            "pdemands" : pdemands
        }

        return render(request,"dashpd.html",context)
    else:
        return redirect("/user/login")

def dashpdupdate(request,id):
    if request.user.is_authenticated:
        demands = Demand.objects.filter( agent = request.user)
        context = {
            "demands" : demands
        }
        demand = get_object_or_404(Demand,id=id)
        form = DemandUForm(request.POST or None,instance= demand)
        if form.is_valid():
            form.save()
            return redirect("pd")
        return render(request,"dashpddetail.html",{"form":form},context)
    else:
        return redirect("/user/login")

def dashserviceupdate(request,id):
    if request.user.is_authenticated:
        services = Service.objects.filter( agent = request.user)
        context = {
            "services" : services
        }
        service = get_object_or_404(Service,id=id)
        form = ServiceUForm(request.POST or None,instance= service)
        if form.is_valid():
            form.save()
            return redirect("dashservices")
        return render(request,"dashservicedetail.html",{"form":form},context)
    else:
        return redirect("/user/login")

def dashboardtest(request):
    return render(request,"dboard/dashboardtest.html")

def account(request):
    return render(request,"dboard/account.html")

