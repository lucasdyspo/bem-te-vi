from turtle import title
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from PIL import Image
from django import forms
import hashlib
from datetime import datetime
from .models import Art
from rest_framework.views import APIView, Response
from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from .serializer import Artserializer
import json
from .models import Art
from django.shortcuts import get_object_or_404
from .models import Art
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
# from django.core import serializers



class ArtApiView(APIView):
    # serializer_class = Artserializer
    # queryset = Art.objects.all()
    
    def get(self, request):
        arts = Art.objects.filter(pk__in=[2, 4, 5])
        serializer = Artserializer(arts, many=True)
        a = serializer.data
        return Response(serializer.data)
    
    
    def post(self, request):
        pass
    
Art_api_view = ArtApiView.as_view()



class ArtViewSet(viewsets.ModelViewSet):
    serializer_class = Artserializer
    queryset = Art.objects.all()


teste_api_art = ArtViewSet.as_view({"get" : "list"})




class ArtDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile_list.html'

    def get(self, request, pk):
        global Art
        art = get_object_or_404(Art, pk=pk)
        serializer = Artserializer(art)
        print(serializer.data)
        return Response({'serializer': serializer, 'Art': art})
        

    def post(self, request, pk):
        art = get_object_or_404(Art, pk=pk)
        serializer = Artserializer(art, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'Art': art})
        serializer.save()
        return redirect('Art-list')

teste = ArtDetail.as_view()

class Img_teste(forms.Form):
    img = forms.ImageField()
    nome = forms.CharField()
    # nome = forms.CharField()
    
    
class artform(forms.Form):
    name = forms.CharField()
    desc = forms.CharField()
    private = forms.CheckboxInput()
     
    
    
    
    
def artAccess(request, idart):
    context = {'idart' : idart}
    
    PATH = '...'
    
    return render(request, 'pageart.html', context=context)





# Create your views here.
def artcreate(request):
    if request.method == 'GET':
        test = artform()
        teste = {'test': test}
        print('esse metodo foi get \n\n\n\n\n\n')
        return render(request, 'artpage.html', context=teste)

    
    
    else:
        
        
        print('esse metodo foi post \n\n\n\n\n\n')
        test = artform((request.POST))
        teste = {}
        unique_name = hashlib.sha256(((test.data['name'] + str(datetime.now())).encode())).hexdigest()
        try:
            art = Art()
            art.encodexname = unique_name
            art.name = test.data['name']
            art.description = test.data['desc']
            
            # art.user_main = 2
            
            art.save()
            print('salvo')
            
        except Exception as e:
            print('error', e)
            
        
        
    
    
    
        return render(request, 'artpage.html', context=teste)





def art_update(request):
    author = request.POST.get('author')
    description = request.POST.get('description')
    art = request.POST.get('art')
    title = request.POST.get('title')
    tag1 = request.POST.get('tag1')
    tag2 = request.POST.get('tag2')
    tag3 = request.POST.get('tag3')
    tag4 = request.POST.get('tag4')
    
    tag5 = request.POST.get('tag5')
    print(author)
    r = str(art)
    print(type(art))
    i = Image.open(art)
    Image.show(i)
    
    
def art_create(request):
    ...
    

    
        
