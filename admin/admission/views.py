from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import studentRegistration
from .models import User

# Create your views here.


def index(request):
    return render(request, "admission/index.html")


def addData(request):
    if request.method == "POST":
        fm = studentRegistration(request.POST)
        if fm.is_valid():
            ss = fm.cleaned_data["sid"]
            nm = fm.cleaned_data["name"]
            st = fm.cleaned_data["Standard"]
            ag = fm.cleaned_data["age"]
            cy = fm.cleaned_data["city"]
            reg = User(sid=ss, name=nm, Standard=st, age=ag, city=cy)
            reg.save()
            fm = studentRegistration()
        stud = User.objects.all().order_by("sid")
        return render(request, "admission/show.html", {"student": stud})
    else:
        fm = studentRegistration()
    return render(request, "admission/add.html", {"form": fm})


def editData(request, id):
    stud = User.objects.get(pk=id)
    return render(request, "admission/edit.html", {"student": stud})


def updateData(request, id):
    student = User.objects.get(pk=id)
    form = studentRegistration(request.POST, instance=student)
    form.save()
    return HttpResponseRedirect("/admission/show")


def showData(request):
    stud = User.objects.all().order_by("sid")
    return render(request, "admission/show.html", {"student": stud})


def deleteData(request, id):
    pi = User.objects.get(pk=id)
    pi.delete()
    return HttpResponseRedirect("/admission/show")
