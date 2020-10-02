from django.urls import path

from . import views

urlpatterns = [
    path("website/players_list.html", views.PlayersView.as_view()),
    #path("<int:pk>/", views.PlayerDetailView.as_view()),
]
