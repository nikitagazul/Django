from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.core.mail import send_mail

from .models import Player, Match, News


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

class MatchesView(ListView):
    model = Match
    context_object_name = 'matches_list'
    queryset = Match.objects.all().order_by('-id')
    template_name = "website/matches_list.html"
    paginate_by = 6

class NewsView(ListView):
    model = News
    context_object_name = 'news_list'
    queryset = News.objects.all().order_by('-id')
    template_name = "website/news_list.html"
    paginate_by = 6

class Sidebars:
    def get_matches(self):
        return Match.objects.all().order_by('-id')[:3]

    def get_news(self):
        return News.objects.all().order_by('-id')[:3]

class IndexView(Sidebars, TemplateView):
    template_name = "website/index.html"

def contact(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        send_mail(subject, message, email, ['nikitagazul@gmail.com'])
        return render(request, 'website/contact.html', {'fname': fname, 'lname':lname})
    else:
        return render(request, 'website/contact.html', {})

class AboutView(TemplateView):
    template_name = "website/about.html"

