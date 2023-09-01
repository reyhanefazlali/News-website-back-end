from django.urls import path
from . import views

app_name='account'
urlpatterns = [
    path('login/',views.login_views,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout_views,name='logout'),
]
