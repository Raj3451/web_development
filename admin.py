from django.contrib import admin
from .models import Pro

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display =("Name","Custo","Date_of_completion")
admin.site.register(Pro,MemberAdmin)