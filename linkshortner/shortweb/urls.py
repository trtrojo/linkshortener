from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShortWeb.as_view(), name='redirect'),
    path('createlink', views.ShortWebCreate.as_view(), name='create_link'),
    path('login', views.LocalLogin.as_view(), name='login'),
    path('logout', views.LocalLogout.as_view(), name='logout'),
    path('createaccount', views.CreateAccount.as_view(), name='create_account')
]

# handler404 = 'shortsvc.views.shortner_404_view'