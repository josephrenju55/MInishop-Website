from django.urls import path
from.import views

urlpatterns = [
    path('',views.home,name='home'),
    path('<slug:c_slug>/',views.home,name='prod_cat'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('search',views.search,name='search')
    
]
