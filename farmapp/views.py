from email.policy import HTTP
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
# import MySQLdb
from .models import Registration,Login,Addcropdetails,Addnews
from django.contrib import messages
from django.db import connection
from django.db.models import Q,Max,Count
from datetime import datetime as date
# con=MySQLdb.connect("localhost","root","","farmer")
# c=con.cursor()
# Create your views here.
def index(request):
    data=Addnews.objects.filter()

    return render(request,"index.html",{"data":data})

def contact(request):
    return render(request,"contact.html")    
def common(request):
    return render(request,"common.html") 
def UserHome(request):
    return render(request,"UserHome.html")        
def login(request):
    msg=""
    try:
        if request.POST :
            uname=request.POST["t1"]
            password=request.POST["t2"]
            data=Login.objects.filter(Q(uname=uname)&Q(password=password))
            print("data=", data[0].role)
            request.session["uname"]=uname
            print("####################################################")
            if(data[0].role=="admin"):
                return HttpResponseRedirect("/Adminviewfarmer")
            elif(data[0].role=="Farmer"):
                return HttpResponseRedirect("/UserHome")
            elif(data[0].role=="Delivary"):
                return HttpResponseRedirect("/delivaryviewcrop")
            else:
                msg="Invalid Username or password"
    except:
        msg="Invalid Username or password"

    return render(request,"login.html",{"msg":msg}) 
def registration(request):
    msg=""
    if request.POST:
        name=request.POST["t1"]
        gender=request.POST["t2"]
        email=request.POST["t3"]
        phone=request.POST["t4"]
        password=request.POST["t5"]
        address=request.POST["t6"]
        # data=Login.objects.get(uname=email)
        # c.execute("select count(*) from login where uname='"+str(email)+"'")
        # data=c.fetchall()
        # if(data):
        if(Login.objects.filter(uname=email).exists()):
            msg="username already exists"
        else:
            obj=Registration.objects.create(name=name,gender=gender,email=email,phone=phone,address=address)
            obj.save()
            obj1=Login.objects.create(uname=email,password=password,role='Farmer')
            obj1.save()
            msg="Registration successfully"
        # else:
        #     msg="Username already exist"

    return render(request,"Farmerregistration.html",{"msg":msg})    
    
def farmerprofile(request):
    msg=""
    uname=request.session["uname"]
    data=Registration.objects.filter(Q(email=uname))
    if request.POST:
        name=request.POST["t1"]
        gender=request.POST["t2"]
        email=request.POST["t3"]
        phone=request.POST["t4"]
        password=request.POST["t5"]
        data=Login.objects.get(uname=email)
        # c.execute("select count(*) from login where uname='"+str(email)+"'")
        # data=c.fetchall()
        if(data):
            obj=Registration.objects.get(email=email)
            obj.name=name
            obj.phone=phone
            obj.save()
            obj1=Login.objects.get(email=email)
            obj1.password=password
            obj1.save()
            msg="Registration successfully"
        else:
            msg="Username already exist"
    return render(request,"Farmerprofile.html",{"msg":msg,"data":data}) 
def Addcropdetails1(request):
    msg=""
    import datetime
    now = datetime.datetime.now()
    lastconnection = now.strftime('%Y-%m-%d')
    uname=request.session["uname"]
    data1=Registration.objects.get(email=uname)

    if request.POST:
        name=request.POST["t1"]
        
        qty=request.POST["t3"]
        status=request.POST["t4"]
        date=request.POST["t5"]
       
        # c.execute("select count(*) from login where uname='"+str(email)+"'")
        # data=c.fetchall()
        
        obj=Addcropdetails.objects.create(fid=data1,name=name,qty=qty,status=status,date=date)
        obj.save()
        msg="Successfully Added"
       
          

    return render(request,"Farmeraddcrop.html",{"msg":msg,"today":lastconnection})
def farmerviewcrop(request):
    uname=request.session["uname"]
    data1=Registration.objects.filter(email=uname)
    cmpid=data1[0].id
    data=Addcropdetails.objects.filter(fid=cmpid)
    return render(request,"farmerviewcrop.html",{"data":data})

def Adminviewcrop(request):
    
    data=Addcropdetails.objects.filter()
    return render(request,"Adminviewcrop.html",{"data":data})
def Adminviewfarmer(request):
    
    data=Registration.objects.filter()
    return render(request,"Adminviewfarmer.html",{"data":data})
def AdminaddNews(request):
    if request.POST:

        data=Addnews.objects.create(title=request.POST["t3"],news=request.POST["t1"])
        data.save()    
    return render(request,"AdminaddNews.html")

def Farmerviewnews(request):
    data=Addnews.objects.filter()
        
    return render(request,"Farmerviewnews.html",{"data":data})
def Adminaddloantype(request):
    if request.POST:
        obj=Loantype.objects.create(type=request.POST["t1"],duration=request.POST["t2"],description=request.POST["t3"],amount=request.POST["t4"])
        obj.save()
    data=Loantype.objects.filter()   
    return render(request,"Adminaddloantype.html",{"data":data})
def deleteloan(request):
    return HttpResponseRedirect("/Adminaddloantype")
def farmerviewloan(request):
    data=Loantype.objects.filter()
    return render(request,"farmerviewloan.html",{"data":data})
def farmerrequestloan(request):
    msg=""
    import datetime
    now = datetime.datetime.now()
    lastconnection = now.strftime('%Y-%m-%d')
    id=request.GET["id"]
    data=Loantype.objects.filter(Q(id=id))
    if request.POST:
        obj1=Registration.objects.get(email=request.session["uname"])
        obj2=Loantype.objects.get(id=id)
        obj3=Loanrequest.objects.create(loanid=obj2,uid=obj1,requestamount=request.POST["t3"],status='Requested',date=request.POST["t4"])
        obj3.save()
        msg="Applied Successfully"
    return render(request,"Farmerrequestloan.html",{"data":data,"msg":msg,"today":lastconnection})
def farmerviewloanstatus(request):
    obj1=Registration.objects.get(email=request.session["uname"])
    data=Loanrequest.objects.filter(Q(uid=obj1))
    return render(request,"Farmerviewloanstatus.html",{"data":data})
def collectcrop(request):
    import datetime
    now = datetime.datetime.now()
    lastconnection = now.strftime('%Y-%m-%d')
    id=request.GET["id"]
    data=Loantype.objects.filter(Q(id=id))
    if request.POST:
        obj1=delivaryboy.objects.get(email=request.session["uname"])
        obj2=Addcropdetails.objects.get(id=id)
        request.session["pay"]=request.POST["t3"]
        obj3=delivary.objects.create(did=obj1,cropid=obj2,amount=request.POST["t3"])
        obj3.save()
        return HttpResponseRedirect("/payment1")
    return render(request,"collectcrop.html",{"data":data,"today":lastconnection})
def delivaryviewcrop(request):
    data=Addcropdetails.objects.filter()
    return render(request,"delivaryviewcrop.html",{"data":data})
def adminviewcropcollection(request):
    data=delivary.objects.filter()
    return render(request,"adminviewcropcollection.html",{"data":data})
def adminadddelivaryboy(request):
    msg=""
    if request.POST:
        obj=delivaryboy.objects.create(name=request.POST["t1"],gender=request.POST["t2"],email=request.POST["t3"],phone=request.POST["t4"])
        obj.save()
        obj1=Login.objects.create(uname=request.POST["t3"],password=request.POST["t5"],role='Delivary')
        obj1.save()
        msg="Saved Successfully"
    return render(request,"adminadddelivaryboy.html",{"data":msg})
def payment1(request):
    msg=""
    count=0
    uname=request.session["uname"]
   
        
    if request.POST:
        card=request.POST.get("test")
        request.session["card"]=card
        cardno=request.POST.get("cardno")
        request.session["card_no"]=cardno
        pinno=request.POST.get("pinno")
        request.session["pinno"]=pinno
        return HttpResponseRedirect("/payment2")
            
    return render(request,"payment1.html",{"msg":msg,"uname":uname})

def payment2(request):
    cno=request.session["card_no"]
    amount=request.session["pay"]
    if request.POST:
        # name=request.POST.get("t1")
        # request.session["m"]=name
        # address=request.POST.get("t2")
        # email=request.POST.get("t3")
        # phno=request.POST.get("t4")
        # n="insert into delivery values('"+str(cno)+"','"+str(name)+"','"+str(address)+"','"+str(email)+"','"+str(phno)+"','"+str(amount)+"')"
        # print(n)
        # c.execute(n)
        # con.commit()
        return HttpResponseRedirect("/payment3")
    return render(request,"payment2.html",{"cno":cno,"amount":amount})

def payment3(request):
    return render(request,"payment3.html")

def payment4(request):
    return render(request,"payment4.html")

def payment5(request):
    cno=request.session["card_no"]
    today = "05/05/2000"
    name = "FarmTech"
    amount = request.session["pay"]
    return render(request,"payment5.html",{"cno":cno,"today":today,"name":name,"amount":amount})
def adminviewloan(request):
    
    data=Loanrequest.objects.filter()
    return render(request,"Adminviewloan.html",{"data":data})
def acceptloan(request):
    id=request.GET["id"]
    data=Loanrequest.objects.filter(id=id).update(status='Accepted')
    return HttpResponseRedirect("/adminviewloan")
def Addfeedback(request):
    if request.POST:
        data=Registration.objects.get(email=request.session["uname"])
        obj=Feedback.objects.create(fid=data,Feedbacks=request.POST["t1"])
        obj.save()
    return render(request,"Addfeedback.html",{"data":data})
def Viewfeedback(request):
    data=Feedback.objects.filter()
    
    return render(request,"Viewfeedback.html",{"data":data})


