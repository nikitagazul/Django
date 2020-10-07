from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name='home'),
    path("about.html", views.AboutView.as_view(), name='about'),
    path("contact.html", views.ContactView.as_view(), name='contact'),
    path("news_list.html", views.NewsView.as_view(), name='news'),
    path("matches_list.html", views.MatchesView.as_view(), name='matches'),
    path("players_list.html", views.PlayersView.as_view(), name='players'),
    # path("<int:pk>/", views.PlayerDetailView.as_view()),

]
