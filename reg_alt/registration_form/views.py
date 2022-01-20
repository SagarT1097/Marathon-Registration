from django.shortcuts import render, redirect
from django import forms
from django.utils import timezone
from registration_form.forms import Reg_page1 , Bib_form
from registration_form.models import Register
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import datetime
import csv
from random import randint
from .render import Render
from django.views.generic import View


@csrf_exempt
def register(request):

    if request.method == "POST":
        form = Reg_page1(request.POST)
        print(request.POST, "Valid Form:", form.is_valid(), form.errors, dir(form.data))

        if form.is_valid():
            print(request.POST, "Valid Form:", form.is_valid(), form.errors, dir(form.data))
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return render(request, "registration_form/register.html", {'forms': form , 'success_reg' : "Registration successful!"})
    else:

        form = Reg_page1()

    return render(request, "registration_form/register.html", {'forms': form})

def bib_update(request):

    if request.method == "POST":
        form = Bib_form(request.POST)


        print(request.POST, "Valid Form:", form.is_valid(), form.errors, dir(form.data))
        if form.is_valid():
            Register.objects.filter(phno=form.data['phno']).update(bibno=form.data['bibno'])
            return render(request, "registration_form/bibupdate.html", {'forms': form,'success_reg' : "Bib successfully allocated! See you on the race day!"})

    else:

        form = Bib_form()

    return render(request, "registration_form/bibupdate.html", {'forms': form})


def bib_search(request):
    str = "Does not exist"
    if request.method == "GET":
        form = Bib_form(request.GET)


        print(request.GET, "Valid Form:", form.is_valid(), form.errors, dir(form.data))
        if form.is_valid():
            if(Register.objects.filter(phno=form.data['phno']).exists()) :
                return render(request,"registration_form/bib_search.html" , {'obj': Register.objects.filter(phno=form.data['phno']) , 'forms':form })
            else :
                return render(request, "registration_form/bib_search.html" , {'message' :str ,'forms':form})

    else:

        form = Bib_form()

    return render(request, "registration_form/bib_search.html", {'forms': form})


def bib_exists(request):

    return render(request,"registration_form/exists.html" , {'obj': Register.objects.filter(phno=form.data['phno'])})

def details_data(request):

    male_count = Register.objects.filter(gender="m").count()
    female_count = Register.objects.filter(gender="f").count()
    total_count = male_count + female_count
    xs_count = Register.objects.filter(teesize="xs").count()
    s_count = Register.objects.filter(teesize="s").count()
    m_count = Register.objects.filter(teesize="m").count()
    l_count = Register.objects.filter(teesize="l").count()
    xl_count = Register.objects.filter(teesize="xl").count()
    bib_count_null = Register.objects.filter(bibno= 0).count()
    bib_count = total_count - bib_count_null
    dic_expr = Register.objects.values_list('expr',flat=True)
    list_expr = []
    list_expr = list(dic_expr)
    e1=e2=e3 = 0
    for i in list_expr:
        if i in range(0,5):
            e1 += 1
        elif i in range(5,10):
            e2 += 1
        else :
            e3 += 1

    dict_dob = Register.objects.values_list('dob',flat=True)
    list_dob = list(dict_dob)
    list_len = len(list_dob)
    list_age = []
    r1=r2=r3=r4 = 0
    for i in dict_dob :
        today = datetime.date.today().year
        age = today - i.year
        list_age.append(age)
    for i in list_age:
        if i in range(0,10):
            r1 += 1
        elif i in range(11,20):
            r2 += 1
        elif i in range(21,30):
            r3 += 1
        else :
            r4 += 1
    params = {
                'mc' : male_count,
                'fc' : female_count,
                'xsc' : xs_count,
                'sc' : s_count,
                'mc' : m_count,
                'lc' : l_count,
                'xlc' : xl_count,
                'reg_c' : total_count,
                'bib_c' : bib_count,
                'begg_count' : e1,
                'inter_count' :e2,
                'pro_count' : e3,
                'age_kid':r1,
                'age_teen':r2,
                'age_yd':r3,
                'age_adults':r4
    }
    return render(request,"line_chart.html" ,params)


def bib_edit(request):

    if request.method == "POST":
        form = Bib_form(request.POST)


        print(request.POST, "Valid Form:", form.is_valid(), form.errors, dir(form.data))
        if form.is_valid():
            Register.objects.filter(phno=form.data['phno']).update(phno=form.data['phno'])
            Register.objects.filter(phno=form.data['emailid']).update(phno=form.data['emailid'])
            Register.objects.filter(phno=form.data['username']).update(phno=form.data['username'])
            Register.objects.filter(phno=form.data['bibno']).update(phno=form.data['bibno'])
            return redirect('/register/bib_edit')

    else:

        form = Bib_form()

    return render(request, "registration_form/bib_edit.html", {'forms': form , 'edit_msg' : "Bib successfully edited! See you on the race day!"})

def export(request):
    register_resource = RegisterResource()
    dataset = person_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="persons.csv"'
    return response

def details_pass(request):

    return render(request, "registration_form/check_pass.html", {})
