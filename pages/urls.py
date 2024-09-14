from django.urls import path
# Import the class that you created in views
from .views import HomePageView, AboutPageView

urlpatterns = [
    path('',HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),

]