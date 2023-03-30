from django.contrib import admin
from .models import HighlightsAdmin, Post, Likes

# Register your models here.
@admin.register(HighlightsAdmin)
class reg_highlights(admin.ModelAdmin):
    readonly_fields = ()


@admin.register(Post)
class reg_post(admin.ModelAdmin):
    readonly_fields = ()

@admin.register(Likes)
class reg_likes(admin.ModelAdmin):
    readonly_fields = ()
