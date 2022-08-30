# Developed by Surfa
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.urls import path
from native import views

app_name = 'native'

urlpatterns = [
    #path('',views.HomePage.as_view(),name='home'),
    path('about/',views.About.as_view(),name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('services/',views.Services.as_view(),name='services'),
    path('gallery/',views.Gallery.as_view(),name='gallery'),
    path('team/',views.Team.as_view(),name='team'),
    path('timetable/',views.Timetable.as_view(),name='timetable'),
    path('bmi/',views.bmi,name='bmi'),
    path('blog/', views.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('classdetail/',views.ClassDetail.as_view(),name='classdetail'),
]

