from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShortWeb.as_view(), name='redirect'),
    path('createlink', views.ShortWebCreate.as_view(), name='create_link')
]

# handler404 = 'shortsvc.views.shortner_404_view'