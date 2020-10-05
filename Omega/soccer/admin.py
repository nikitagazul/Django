from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News, Player, Match

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("fname", "lname", "number", "get_image")
    list_display_links = ("fname", "lname", "number",)
    search_fields = ("fname", "lname",)
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} class="img-fluid" width="96" height="128"')

    get_image.short_description = "Picture"


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "date")
    list_display_links = ("title", "date",)
    list_filter = ("date",)
    search_fields = ("title", "date",)

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ("team_name1", "score1", "score2", "team_name2")
    list_display_links = ("team_name1", "score1", "score2", "team_name2",)
    search_fields = ("team_name1", "team_name2")

admin.site.site_title = "MFC Omega Three"
admin.site.site_header = "MFC Omega Three"
# Register your models here.
