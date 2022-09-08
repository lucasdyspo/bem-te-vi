from django.contrib import admin
from .models import Art, favorites, Likes
# Register your models here.
@admin.register(Art)
class arts(admin.ModelAdmin):
    list_display=("name", "user_main", "created_date")
    readonly_fields = ()
    
    
    
@admin.register(favorites)
class fav(admin.ModelAdmin):
    readonly_fields = ()



@admin.register(Likes)
class likes(admin.ModelAdmin):
    readonly_fields = ()
    