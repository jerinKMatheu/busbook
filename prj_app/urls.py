from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='Index'),
    path('find_bus',views.find_bus,name='Find_bus'),
    path('current_location_map',views.map_view,name='current_location_map'),
    path('register',views.user_registration,name='register'),
    path('modal-login', views.modal_login_page, name='modal_login_page'),
    path('system-admin',views.system_admin,name='adminpage'),
    path('bus-provider',views.bus_provider,name='provider'),
    path('logout',views.logout_view,name='logout'),
    path('verify-otp', views.verify_otp_view, name='verify_otp'),
    path('adminpanel/', views.Adminview.as_view(),name="adminpage"),

]
