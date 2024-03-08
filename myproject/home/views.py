from django.shortcuts import render,HttpResponse,redirect
from . models import Student

# Create your views here.
def index(request):
    data={
        'stu':Student.objects.all()
    }
    print(data)
    return render(request,'index.html',data)
def addStudent(request):
    return render(request,'addStudent.html')
def insertStudent(request):
    if request.method=="POST":
        name=request.POST.get('sname')
        place=request.POST.get('splace')
        city=request.POST.get('scity')
        query=Student(name=name,place=place,city=city)
        query.save()
    return redirect("/")
def delete(request,id):
    dlt=Student.objects.get(id=id)
    dlt.delete()
    return redirect("/")

def edit(request,id):
    obj = Student.objects.get(id=id)
    return render(request,'edit.html',{'data':obj})

def update(request,id):
    if request.method=="POST":
        name=request.POST.get('sname')
        place=request.POST.get('splace')
        city=request.POST.get('scity')
        print(name)
        edit=Student.objects.get(id=id)
        edit.name=name
        edit.place=place
        edit.city=city
        edit.save()
        return redirect("/")
    
        










def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')