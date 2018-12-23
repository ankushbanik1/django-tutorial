
from django.views.generic import TemplateView
from .forms import Homeforms
from django.shortcuts import render,redirect
from home.models import Post
from django.contrib.auth.models import User



class homeview(TemplateView):
    template_name='home/home.html'



    def get(self,request):
        form =Homeforms()
        posts=Post.objects.all()
        users=User.objects.exclude(id=request.user.id)

        args={'form':form,'posts':posts,'users':users}
        return render(request,self.template_name,args)
        


    def post(self,request):
        form= Homeforms(request.POST)
        if form.is_valid():
            form.save(commit=False)
            post.user=request.user
            post.save()
            text= form.cleaned_data['post'] 
            form= Homeforms()
            return redirect('home')



        args={'form':form , 'text':text }
        return render(request,self.template_name,args)