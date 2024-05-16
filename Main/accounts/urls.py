from django.urls import path
from accounts import views
app_name = 'accounts'

urlpatterns = [
    path('LoginRegister/',views.LoginRegisterView.as_view(),name='LoginRegister'),
    path('LoginRegisterVerify/', views.LoginRegisterVerifyView.as_view(), name='LoginRegisterVerify'),
    path('LogOut/',views.LogOutView.as_view(),name='LogOut'),
    path('Profile/',views.ProfileView.as_view(),name='Profile'),

]