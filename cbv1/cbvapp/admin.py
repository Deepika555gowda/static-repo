from django.contrib import admin

# Register your models here.
from cbvapp.models import student
class studentAdmin(admin.ModelAdmin):
    l=['name','number','marks','place']
admin.site.register(student,studentAdmin)
