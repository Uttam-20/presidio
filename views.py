from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context,Template,loader
from .models import Buyer,Seller,Buying,Selling
# Create your views here.
def Register(request):
    name=request.GET["name"]
    password=request.GET["pass"]
    mobile=request.GET["mobile"]
    status=request.GET["status"]
    if status=="seller":
        mydata=Seller.objects.filter(name=name,password=password,mobile=mobile).values()
    if status=="buyer":
        mydata=Buyer.objects.filter(name=name,password=password,mobile=mobile).values()
    if mydata:
        return HttpResponse("User already exists")
    if status=="buyer":
        mymember=Buyer(name=name,password=password,mobile=mobile)
        mymember.save()
    if status=="seller":
        mymember=Seller(name=name,password=password,mobile=mobile)
        mymember.save()
    return HttpResponse("Registration Successful")
def login(request):
    name=request.GET["name"] 
    password=request.GET["pass"]
    status=request.GET["status"]
    if status=="seller":
        mydata=Seller.objects.filter(name=name,password=password)
    if status=="buyer":
        mydata=Buyer.objects.filter(name=name,password=password)
    if not mydata:
        return HttpResponse("Invalid Login Details")
    if status=="seller":
        template=loader.get_template('Seller.html')
        mydat=mydata[0]
        context={
            'mydat':mydata[0].name
        }
        return HttpResponse(template.render(context,request))
    if status=="buyer":
        template=loader.get_template('Buyer.html')
        mydat=mydata[0]
        context={
            'mydat':mydata[0].name,
        }
        return HttpResponse(template.render(context,request))

def Sell(request):
    mydata=Selling.objects.all().values()
    template=loader.get_template('Selling.html')
    context={
        'mydata':mydata,
    }
    return HttpResponse(template.render(context,request))
def Buy(request):
    mydata=Buying.objects.all().values()
    template=loader.get_template("Buying.html")
    context={
        'mydata':mydata,
    }
    return HttpResponse(template.render(context,request))
def sign(request):
    template=loader.get_template('sign.html')
    return HttpResponse(template.render())
def log(request):
    template=loader.get_template('log.html')
    return HttpResponse(template.render())
def requesthome(request):
    name=request.GET["name"]
    typ=request.GET["type"]
    room=request.GET["room"]
    mobile=request.GET["mobile"]
    mydata=Buying(name=name,Htype=typ,rooms=room,mobile=mobile)
    mydata.save()
    return HttpResponse("Saved")
def sellhome(request):
    hno=request.GET["hno"]
    typ=request.GET["type"]
    room=request.GET["room"]
    place=request.GET["place"]
    cont=request.GET["contact"]
    mydata=Selling(Hno=hno,Hadrr=place,Htype=typ,rooms=room,Contact=cont)
    mydata.save()
    return HttpResponse("Saved")
def showbuy(request):
    template=loader.get_template('buy.html')
    return HttpResponse(template.render())
def showsell(request):
    template=loader.get_template('sell.html')
    return HttpResponse(template.render())
