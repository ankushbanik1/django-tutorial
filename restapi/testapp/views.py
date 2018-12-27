from django.shortcuts import render
from django.http import HttpResponse


def emp_data(request):
    emp_data={
        'eno':100,
        'ename':"ankush",
        'esal':10000,
        'add':"chandigarh",

    }
    resp='<h1>Employee number:{}<br> Employee name:{}<br> Employee Salary:{} <br>Employee Address:{}<br></h1>'.format(emp_data['eno'],emp_data['ename'],emp_data['esal'],emp_data['add'])

    return HttpResponse(resp)


def emp_data_json(request):
    emp_data={
        'eno':100,
        'ename':"ankush",
        'esal':10000,
        'add':"chandigarh",

    }

    return HttpResponse(resp)    