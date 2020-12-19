from django.contrib import admin
from app.models import Student,Contact_Us,Category
# Register your models here.

admin.site.site_header="My website | Himanshu"

class studentAdmin(admin.ModelAdmin):
    list_display=['name','roll_no','email','gender']
    search_fields=['email']
    list_filter=['name','roll_no','email','gender']
    list_editable=["email"]

class contactAdmin(admin.ModelAdmin):
    list_display=['id','added_on','name','subject']
    list_editable=['name']


class CategoryAdmin(admin.ModelAdmin):
    list_display=["name","cover_pic","description"]

admin.site.register(Student,studentAdmin)
admin.site.register(Contact_Us,contactAdmin)
admin.site.register(Category,CategoryAdmin)