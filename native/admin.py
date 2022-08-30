# Developed by Surfa
from django.contrib import admin
from .models import Gallery, Trainers, Contact, Bmi
from native.forms import ContactForm
# Register your models here.

class BmiAdmin(admin.ModelAdmin):
    list_display = ('user', 'weight', 'height', 'bmi', 'date')

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','image', 'image2',)
    search_fields = ['title','image',]

class TrainersAdmin(admin.ModelAdmin):
    list_display = ('title', 'name','image', 'trainer_email','fb_account','youtube_account','insta_account')
    search_fields = ['title', 'name','image']

class ContactAdmin(admin.ModelAdmin):
    # list_display = ('name', 'email','website','message')
    contact = ContactForm
    search_fields = ['name', 'email','website','message']

admin.site.register(Gallery, PostAdmin)
admin.site.register(Trainers,TrainersAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Bmi, BmiAdmin)

