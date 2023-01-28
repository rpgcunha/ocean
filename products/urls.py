from django.urls import path
from . import views

urlpatterns = [
    path('betting-security/', views.betting, name='betting'),
    path('pre-sale/', views.preSale, name='presale'),
    path('token/', views.token, name='token'),
    path('royalty-cards/', views.cards, name='cards'),
    path('market-place/', views.market, name='market'),
    path('road-map/', views.roadMap, name='roadmap'),
    path('available-betting-modes/', views.modes, name='modes'),
]