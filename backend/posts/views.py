from django.shortcuts import render
from common.views import RestViewSet
from .serializer import HighlightsSerializer, Commentsserializer, Postserializer
from .models import Post, HighlightsAdmin
from rest_framework.generics import *
# Create your views here.
from django.contrib.auth.decorators import login_required
from rest_framework.generics import *
from rest_framework import viewsets, status



class ArtView(ListAPIView):


    list_arts =  [5]
    serializer_class = Postserializer
    queryset = Post.objects.filter(pk__in=(list_arts)).prefetch_related('favorites')
    # print(dir(queryset[0]))



class HighlightsView(ListAPIView):
    serializer_class = HighlightsSerializer
    queryset = HighlightsAdmin.objects.all().order_by('-pk')[:1]


# def search_view(request, term):
#     results = MyModel.objects.filter(name__icontains=term)
#     # Faz algo com os resultados da pesquisa
#     return render(request, 'search_results.html', {'results': results})


# def search_view(request):
#     search_term = request.GET.get('q')
#     results = MyModel.objects.filter(name__icontains=search_term)
#     # Faz algo com os resultados da pesquisa
#     return render(request, 'search_results.html', {'results': results})





class Commentspageapi(viewsets.ViewSet):
    basename = 'comment'
    serializer_class = Commentsserializer
    # list_arts = [2, 4, 6]
    # queryset = Comment.objects.filter(art__in=(list_arts))


    def get_queryset(self):
        artid = self.kwargs.get('pk')
        queryset = Comment.objects.filter(art=(artid))

        return queryset




class Api_post(ListAPIView):
    serializer_class = Postserializer
    queryset = Post.objects.all()


