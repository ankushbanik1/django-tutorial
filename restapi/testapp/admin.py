from django.contrib import admin
from testapp.models import employee


class employeedata(admin.ModelAdmin):
    list_display=['id','eno','ename','esal','eddr']
admin.site.register(employee,employeedata)