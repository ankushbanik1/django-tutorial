from django.contrib import admin

# Register your models here
# .
from .forms import statusForm
from .models import status


class statusFormadmin(admin.ModelAdmin):
    list_display=['user','__str__','image']
    # class Meta:
    #     model= status
    form=statusForm
admin.site.register(status,statusFormadmin)
