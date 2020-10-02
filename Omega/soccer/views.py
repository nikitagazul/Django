from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import View

from .models import Player


class PlayersView(ListView):
        model = Player
        context_object_name = 'players_list'
        queryset = Player.objects.all()
        template_name = "website/players_list.html"

#class PlayerDetailView(View):
 #   def get(self, request, pk):
  #      player = Player.objects.get(id=pk)
   #     return render(request, "players/players_list.html", {"players_list": player})
# Create your views here.
