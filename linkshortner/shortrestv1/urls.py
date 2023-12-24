from django.urls import path
from . import views

urlpatterns = [
    path('url', views.SingleURL.as_view(), name='singleshortnerurl'),
    path('url/<str:shortened_id>', views.SingleURL.as_view(), name='singleshortnerurl'),
]

# handler404 = 'shortsvc.views.shortner_404_view'