from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Usuario)
class usuarioadmin(admin.ModelAdmin):
    list_display = ('vulgo', 'id', 'has_photo')
    readonly_fields = ('senha',)
    
    def has_photo(self, obj):
        return bool(obj.photo)
    
    has_photo.short_description = 'foto disponivel'
    
    def count_arts(self, obj):
        return 0
    
@admin.register(Img_test)
class bancodeimagens(admin.ModelAdmin):
    readonly_fields = ()


@admin.register(Friend)
class amizade(admin.ModelAdmin):
    readonly_fields = ()



@admin.register(FriendshipRequest)
class amizadepedido(admin.ModelAdmin):
    readonly_fields = ()