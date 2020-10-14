from django.db import models

# Create your models here.
class News(models.Model):
    #News
    image = models.ImageField(verbose_name="Фото", upload_to="news/")
    title = models.CharField(verbose_name="Название", max_length=30)
    date = models.DateField(verbose_name="Дата")
    description = models.TextField(verbose_name="Описание", max_length=265)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class Player(models.Model):
    #Players
    image =models.ImageField(verbose_name="Фото", upload_to="player/")
    fname = models.CharField(verbose_name="Имя", max_length=15)
    lname = models.CharField(verbose_name="Фамилия", max_length=15)
    birth = models.DateField(verbose_name="Дата Рождения")
    position = models.CharField(verbose_name="Позиция", max_length=12)
    number = models.IntegerField(verbose_name="Номер", null=True, blank=True)
    description = models.TextField(verbose_name="Биография")

    def __str__(self):
        return self.fname;
        return self.lname;

    class Meta:
        verbose_name = 'Игрока'
        verbose_name_plural = 'Игроки'

class Match(models.Model):
    #Matches
    image1 = models.ImageField(verbose_name="Фото первой команды", upload_to="match/")
    team_name1 = models.CharField(verbose_name="Название первой команды", max_length=30)
    team_country1 = models.CharField(verbose_name="Страна первой команды", max_length=20)
    score1 = models.IntegerField(verbose_name="Голов первой", null=True, blank=True)
    score2 = models.IntegerField(verbose_name="Голов второй", null=True, blank=True)
    image2 = models.ImageField(verbose_name="Фото второй", upload_to="match/")
    team_name2 = models.CharField(verbose_name="Название второй команды", max_length=30)
    team_country2 = models.CharField(verbose_name="Страна второй команды", max_length=20)

    def __str__(self):
        return self.team_name1;
        return self.team_country1;
        return self.score1;
        return self.team_name2;
        return self.team_country2;
        return self.score2;

    class Meta:
        verbose_name = 'Игру'
        verbose_name_plural = 'Игры'