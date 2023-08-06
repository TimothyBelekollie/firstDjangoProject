from django.urls import path
#from .views import homePageView
from .views import HomePageView, AboutusView

# I am going to define my url patterns

urlpatterns = [
  # path('',homePageView,name='home') 
  path('',HomePageView.as_view(), name='home'),
  path('aboutus/',AboutusView.as_view(), name='aboutus'),
]
