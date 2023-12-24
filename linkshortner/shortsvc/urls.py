from django.urls import path
from . import views

urlpatterns = [
    path('<str:shortened_id>', views.ShortnerView.as_view(), name='redirect'),
]

# handler404 = 'shortsvc.views.shortner_404_view'