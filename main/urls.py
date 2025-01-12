from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('meal/',views.meal,name='meal'),
    path('qa/',views.qa,name='qa'),
    path('finapply/',views.finapply,name='finapply'),  
    path('fee/',views.fee,name='fee'), 
    path('staffs/',views.staffs,name='staffs'), 
    path('booking/', views.booking, name='booking'),
    path('opinion/', views.opinion, name='opinion'),
    path('application/', views.application, name='application'),
    path('facilities/', views.facilities, name='facilities'),    
    path( 'services/', views.services, name = 'services' ),
    path( 'movein/', views.movein, name = 'movein' ),
    path( 'qualification/', views.qualification, name = 'qualification' ),
    path( 'map/', views.map, name = 'map' ),
]

