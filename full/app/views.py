from django.shortcuts import render
from app.models import Student,Category
from django.http import HttpResponse

# Create your views here.
def singup_view(request):
    """ Signup function """

# Data Retrive from Database
    name_data=Student.objects.all().order_by("-id")
    
# when we put data in Form Data print in consol  
    print("data=",request.POST)

# Data post to databse
    if request.method=='POST':
        fn=request.POST['firstname']
        em=request.POST['email']
        rol=request.POST['Rollno']
        fe=request.POST['Fee']
        gen=request.POST['Gender']
        ad=request.POST['Address']
        dat=Student(name=fn ,email=em,roll_no=rol,fee=fe,gender=gen,address=ad )
        dat.save()
        res="Dear {} thanks for singup".format(fn)
        return render(request,"singup.html",{"status":res, "namelist":name_data})

    return render(request,'singup.html',{"namelist":name_data})

def category_view(request):
    cat_data=Category.objects.all()
    return render(request,'profile.html',{"cat_data":cat_data})    