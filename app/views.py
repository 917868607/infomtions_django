from django.shortcuts import render, redirect
from .models import Mysql_info


# Create your views here.

def index(request):
    result = Mysql_info.objects.all()
    return render(request, 'index.html', {'result': result})

def update_info(request):
    if request.method=='GET':
        if request.GET.get('id','res')=='res':
            return render(request, 'add_form.html')
        else:
            id = request.GET['id']
            result1 = Mysql_info.objects.get(id=id)
            return render(request,'add_form.html',{'result1':result1})
    else:
        result = Mysql_info()
        if request.GET.get('id',1) != 1:
            id = request.GET['id']
            result = Mysql_info.objects.get(id=id)
        result.address =request.POST['home']
        result.student =request.POST['classmate']
        result.name =request.POST['name']
        result.motto =request.POST['life_info']
        result.profession =request.POST['job']
        result.profession_info =request.POST['job_info']
        result.student_info =request.POST['classmate_info']
        result.address_info =request.POST['home_info']
        result.school_info =request.POST['school_info']
        result.school =request.POST['school']
        result.save()
        return redirect('/app/')

def del_info(request):
    id = request.GET['id']
    Mysql_info.objects.get(id=id).delete()
    return redirect('/app/')

def about_me(request):
    id = request.GET['id']
    result = Mysql_info.objects.get(id=id)
    print(result)
    return render(request,'about_me.html',{'result':result})