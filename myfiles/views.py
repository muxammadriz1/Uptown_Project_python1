import datetime

from django.db.models import Q
from django.shortcuts import render
from myfiles.models import *
# Create your views here.

def index(malumot):
    if malumot.method=="POST":
       text = malumot.POST.get('matn')
       soz = str(text).strip()
       qidirish = Q(Nomi__startswith=soz)| Q(Manzil__startswith=soz)| Q(Eski_Narxi__startswith=soz)| Q(Yangi_Narxi__startswith=soz)| Q(Xonalar_startswith=soz)| Q(Hammomlar__startswith=soz)| Q(Maydon__startswith=soz)| Q(Maydon__startswith=soz)| Q(vaqt__startswith=soz)

       servislar = Service.objects.filter(qidirish)
       return render(malumot, 'index.html', {"services": servislar})
    else:

       servislar = Service.objects.all().order_by('-vaqt')[:3]
       return render(malumot, 'index.html', {"services": servislar})


def agent(malumot):
    servislar = Service.objects.all()
    contact = {
        "servic":servislar
    }
    return render(malumot,'agent.html',contact)

def properties(malumot):
    servislar = Service.objects.all()
    contact = {
        "servic":servislar
    }
    return render(malumot,'properties.html',contact)

def contact(malumot):
    if malumot.method == "POST":
        ism = malumot.POST.get('ism')
        gmail = malumot.POST.get('mail')
        fan = malumot.POST.get('subject')
        xabar = malumot.POST.get('message')
        vaqt = datetime.datetime.now()
        Murojat(ism=ism, mail=gmail, subject=fan, massage=xabar, vaqt=vaqt).save()
    servislar = Service.objects.all()
    contact = {
        "servic":servislar
    }
    return render(malumot, 'contact.html', contact)

def properties_single(malumot):
    servislar = Service.objects.all()
    contact = {
        "servic":servislar
    }
    return render(malumot,'properties_single.html',contact)