from django.urls import path
from .views import HelloworldView

urlpatterns = [
    path('hello/', HelloworldView.as_view(), name='hello'),
]