from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name='home'),
    path("about", views.AboutView.as_view(), name='about'),
    path("contact", views.ContactView.as_view(), name='contact'),
    path("news", views.NewsView.as_view(), name='news'),
    path("matches", views.MatchesView.as_view(), name='matches'),
    path("team", views.PlayersView.as_view(), name='players'),
    # path("<int:pk>/", views.PlayerDetailView.as_view()),

]
