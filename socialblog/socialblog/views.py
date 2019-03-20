from django.shortcuts import render

from django.views.generic import TemplateView
# def home(request):
#     return render(request, 'index.html')

class home(TemplateView):
    template_name='index.html'
class thanks(TemplateView):
    template_name='page/thanks.html'
class test(TemplateView):
    template_name='page/test.html'
