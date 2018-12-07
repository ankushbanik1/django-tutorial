from django.contrib import admin
from.models import Language,Paradigm,Programmer,Userprofile



admin.site.register (Language)
admin.site.register (Programmer)

admin.site.register (Paradigm)


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display=('user','user_info','phone_number')

    def user_info(self,object):
        return object.city

    def get_queryset(self,request):
        Queryset = super(UserProfileAdmin,self).get_queryset(request)
        Queryset= Queryset.order_by('city')
        return Queryset    
      

admin.site.register(Userprofile,UserProfileAdmin)
