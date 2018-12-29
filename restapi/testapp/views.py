from django.shortcuts import render
from django.http import HttpResponse
import json
from testapp.mixin import HttpResponseMixin
from testapp import mixin
from django.http import JsonResponse
from django.views.generic import View
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
    return JsonResponse(emp_data)    


    
def emp_data_json2(request):
    emp_data={
        'eno':100,
        'ename':"ankush",
        'esal':10000,
        'add':"chandigarh",

    }
    json_data=json.dumps(emp_data)
    return HttpResponse(json_data,content_type='application/json')   


class jsonCBV(HttpResponseMixin,View):
    def get(self,requset,*args,**kwargs):

        json_data=json.dumps({'hello'})
        return self.render_to_httpresponse(json_data)   


        
