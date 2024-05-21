from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Croud

# Create your views here.

def home(req):
    data=Croud.objects.all()
    return render(req,'Base.html',{'key':data})
def croud(req):
    if(req.method=='GET'):
        return render(req,'new_add.html')
    else:
        name=req.POST.get('name')
        email=req.POST.get('email')
        phone=req.POST.get('phone')
        sal=req.POST.get('sal')
        objects=Croud(name=name,email=email,phone=phone,sal=sal)
        objects.save()
        data=Croud.objects.all()
        return render(req,'Base.html',{'key':data})

def delete_croud(req):
    eid=req.GET.get('eid')
    obj=Croud.objects.filter(id=eid)
    obj.delete()
    data=Croud.objects.all()
    return render(req,'Base.html',{'key':data})

def updateEmployee(req):
    #print(req.method)
    if req.method=="GET":
        eid = req.GET.get('eid')
        obj = Croud.objects.get(id=eid)    
        return render(req,"update.html",{"key":obj})
    else:
        obj = Croud()
        obj.id = req.POST.get('id')    
        obj.name = req.POST.get('name') 
        obj.email = req.POST.get("email")   
        obj.phone = req.POST.get("phone")
        
        obj.sal = float(req.POST.get("sal"))
        obj.save() 
        data=Croud.objects.all()
        return render(req,'Base.html',{'key':data})
        
    


