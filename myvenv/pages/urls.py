from django.urls import path
from .views import homePageView

# I am going to define my url patterns

urlpatterns = [
   path('',homePageView,name='home') 
]
