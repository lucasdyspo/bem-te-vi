from .models import Art
from rest_framework import serializers
from django.dispatch import Signal



class Artserializer(serializers.ModelSerializer):
       
    class Meta:
        model = Art
        fields = '__all__'

        
        
    
        
        
        

