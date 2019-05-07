from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView
# def home(request):
#     return render(request, 'index.html')

class home(TemplateView):
    template_name='index.html'
class thanks(TemplateView):
    template_name='page/thanks.html'
class test(TemplateView):
    template_name='page/test.html'

class profile(TemplateView):
    template_name='page/profile.html'
@login_required    
def your_view(request):
    ''' This could be your actual view or a new one '''
    # Your code
    if request.method == 'GET': # If the form is submitted

        search_query = request.GET.get('search_box', None)
            