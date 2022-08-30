# Developed by Surfa

from email import message_from_string
from django.conf import settings
from telnetlib import GA
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.views import generic
from blog.models import Post
from native.models import Gallery, Trainers, Bmi
from native.forms import ContactForm
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

class HomePage(generic.ListView):
    queryset = Trainers.objects.all()
    template_name = 'index.html'


# send with sengrid

# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             email_subject = f'New contact {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
#             email_message = form.cleaned_data['message']
#             send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAIL)
#             return render(request, 'contact.html')
#     form = ContactForm()
#     context = {'form': form}
#     return render(request, 'contact.html', context)


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact request submitted successfully.')
            return render(request, 'contact.html', {'form': ContactForm(request.GET)})
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)




class Services(TemplateView):
    template_name = 'services.html'



class Gallery(generic.ListView):
    queryset = Gallery.objects.all()
    template_name = 'gallery.html'


class Team(generic.ListView):
    queryset = Trainers.objects.all()
    template_name = 'team.html'

class Timetable(TemplateView):
    template_name = 'class-timetable.html'

class ClassDetail(TemplateView):
    template_name = 'class-details.html'


class BMI(TemplateView):
    template_name  = 'bmi-calculator.html'


class Blog(DetailView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    def get_queryset(self):
        return super().get_queryset()
    
    template_name = 'blog.html'


class BlogDetail(DetailView):
    template_name = 'blog-details.html'


class About(generic.ListView):
    queryset = Trainers.objects.all()
    template_name = 'about-us.html'
    



class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/post_index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


def bmi(request):
    context = {}
    if request.method=="POST":
        weight_metric = request.POST.get("weight-metric")
        weight_imperial = request.POST.get("weight-imperial")
        if weight_metric:
            weight = float(request.POST.get("weight-metric"))
            height = float(request.POST.get("height-metric"))
        elif weight_imperial:
            weight = float(request.POST.get("weight-imperial"))/2.205
            height = (float(request.POST.get("feet"))*30.48 + float(request.POST.get("inches"))*2.54)/100
        bmi = (weight/(height**2))
        save = request.POST.get("save")
        if save == "on":
            Bmi.objects.create(user=request.user,weight=weight, height=height, bmi=round(bmi))
        if bmi < 16:
            state = "Severe Thinness"
        elif bmi > 16 and bmi < 17:
            state = "Moderate Thinness"
        elif bmi > 17 and bmi < 18:
            state = "Mild Thinness"
        elif bmi > 18 and bmi < 25:
            state = "Normal"
        elif bmi > 25 and bmi < 30:
            state = "Overweight"
        elif bmi > 30 and bmi < 35:
            state = "Obese Class I"
        elif bmi > 35 and bmi < 40:
            state = "Obese Class II"
        elif bmi > 40:
            state = "Obese Class III"
        context["bmi"] = round(bmi)
        context["state"] = state
    return render(request, "bmi-calculator.html", context)