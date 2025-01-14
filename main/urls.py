from django.urls import path
from . import views
from .views import meal_list

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
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
    path( 'map/', views.map, name = 'map' ),
    path( 'meal/', views.meal_list, name='meal'),
    path( 'contactus/', views.contactus, name='contactus' ),
]

