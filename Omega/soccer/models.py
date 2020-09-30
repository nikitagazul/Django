from django.db import models

# Create your models here.
class News(models.Model):
    #News
    image = models.ImageField("Image", upload_to="news/")
    title = models.CharField("Title", max_length=30)
    date = models.CharField("Date", max_length=12)
    description = models.TextField("Description")
    url = models.SlugField(max_length=160, unique=True)

class Player(models.Model):
    #Players
    image =models.ImageField("Image", upload_to="player/")
    fname = models.CharField("First Name", max_length=15)
    lname = models.CharField(verbose_name="Last Name", max_length=15)
    position = models.CharField("Position", max_length=12)
    number = models.IntegerField("Number")
    description = models.TextField("Description")

    def __str__(self):
        return self.fname;
        return self.lname;

class Match(models.Model):
    #Matches
    image1 = models.ImageField("Image", upload_to="match/")
    team_name1 = models.CharField(verbose_name="First Team Name", max_length=30)
    team_country1 = models.CharField(verbose_name="First Team Country", max_length=20)
    result = models.CharField("Result", max_length=5)
    image2 = models.ImageField("Image", upload_to="match/")
    team_name2 = models.CharField(verbose_name="Second Team Name", max_length=30)
    team_country2 = models.CharField(verbose_name="Second Team Country", max_length=20)

    def __str__(self):
        return self.team_name1;
        return self.team_country1;
        return self.team_name2;
        return self.team_country2;