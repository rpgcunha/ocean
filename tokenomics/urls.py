from django.urls import path
from . import views

urlpatterns = [
    path('$ocean/', views.ocean),
    path('royalty-cards-details/', views.cardsDetails, name='cardsdetails'),
    path('token-distribution/', views.distribution, name='distribution'),
    path('contracts/', views.contracts, name='contracts'),
]