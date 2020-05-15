from django.urls import path,re_path
from django.conf.urls import url
from . import views


urlpatterns = [
    # re_path(r'^$', views.index,name='index'),
    re_path(r'^$', views.index,name='index'),
    re_path(r'^register$',views.RegistrationView.as_view(),name='register'),
    re_path(r'^login$',views.LoginView.as_view(),name='login'),
    path('activate/<uidb64>/<token>',views.ActivationAccountView.as_view(),name='activate')
]
