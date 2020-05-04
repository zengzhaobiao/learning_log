from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

app_name = 'users'

#修改模板路径
# LoginView.template_name = 'users/login.html'

urlpatterns = [
    path('login/',LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('register/',views.register,name='register'),
]