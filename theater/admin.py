from django.contrib import admin

# Register your models here.

from .models import Theater

class TheaterAdmin(admin.ModelAdmin):
    list_display = ["id","title","director", "producer", "production_date", "release_date", "create_date", "publish_date"]


admin.site.register(Theater, TheaterAdmin)