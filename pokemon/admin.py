from django.contrib import admin
from .models import Pokemon
# Register your models here.
admin.site.register(Pokemon)
# class PokemonAdmin (Pokemon):

class PokemonAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "hp", "active")
    list_filter = ("active",)
    list_display_links = ("id", "name")
    fieldsets = (
        (None,
         {"fields":
             ("name",
              "type",
              "hp",
              "active")
             
             }),
        (
            "Localizations",
            {
                "classes":
                    ("collapse",),
                "fields":
                    ("name_fr",
                     "name_jp",
                     "name_ar"),
            },
        ),
    )
    