from rest_framework.views import APIView, Response
from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from art.serializer import Artserializer
import json
from art.models import Art
from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render

# Create your views here.
pula = "\n\n\n\n\n\n"

def search(request, search):
    context = {'search':search}
    
    return render(request, 'search_page.html', context=context)
    
    
    
def testezin(request, search):
    context = {'search':search}
    
    return render(request, 'search_page.html', context=context)
    
class Homeview(APIView):    
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home.html'
    queryset = Art.objects.filter(pk__in=[2, 4, 5])
    def get(request, context=None):
        arts = Art.objects.filter(pk__in=[2, 4, 5])
        strr = "{%cycle 'paiiiiiiiio' 'na cutaaaaaaaa' %}"
        
        return Response({'arts': arts, 'strr':strr})

home = Homeview.as_view()

# class ArtDetail(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'profile_list.html'

#     def get(self, request, pk):
#         global Art
#         art = get_object_or_404(Art, pk=pk)
#         serializer = Artserializer(art)
#         print(serializer.data)
#         return Response({'serializer': serializer, 'Art': art})
        

#     def post(self, request, pk):
#         art = get_object_or_404(Art, pk=pk)
#         serializer = Artserializer(art, data=request.data)
#         if not serializer.is_valid():
#             return Response({'serializer': serializer, 'Art': art})
#         serializer.save()
#         return redirect('Art-list')

# teste = ArtDetail.as_view()



def settings(request):
    """accounts
    privacity
    connected apps
    edit email and password"""
    
    
    return(render(request, 'mysettings.html'))



def social(request):
    nome = ['paulo moreira', 'espetacular', 'o auto da compadecida', 'ai moi vida', 'pio nex', 'utimame' ]
    context = {'nomes' : nome}
    return render(request, 'social.html', context=context)
    
    
def list_favorites(request):
    return render(request, 'favorites.html')


def myuser(request):
    return render(request, 'myuser.html')


def myinsights(request):
    return render(request, 'myinsights.html')


