from django.shortcuts import render
from common.views import RestViewSet
from .serializer import HighlightsSerializer, Commentsserializer, Postserializer, LikeSerializer
from .models import Post, HighlightsAdmin, Likes
from users.models import User
from rest_framework.generics import *
# Create your views here.
from django.contrib.auth.decorators import login_required
from rest_framework.generics import *
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.views import APIView, Response
from django.views.decorators.csrf import csrf_exempt
from colorama import *
from django.http import HttpResponse
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import download
import sys
import os
from django.db.models import Q


class recom:
    def __init__(self, term, lang=None):

        download('stopwords')


        pula = '\n\n\n\n\n\n\n\n\n'
        if lang == None:
            self.lang = 'portuguese'
        else:
            self.lang = lang

        stop_words = set(stopwords.words(self.lang))
        print(self.lang, pula, stop_words)


        self.stemmer = SnowballStemmer(self.lang)

        print(self.stemmer, pula)

        tokens = []

        for li in (term.split()):
            tokens.append(li)


        print(self.stemmer, pula, tokens)

        self.stop_words = stop_words

        self.tokens = [token for token in tokens if not token in self.stop_words]
        self.stemmed_tokens = [self.stemmer.stem(token) for token in tokens]

        print(self.stemmed_tokens)



# po = recom('sala pro quarto filhao')




class pull:
    def __init__(self, user):
        self.user = user




class Posts_man:

    search_limit = 3
    random_limit = 10

    def search_by_query(self, query):
        # title_posts = Post.objects.filter(title__icontains=query)

        # desc_posts = Post.objects.filter(description__icontains=query)


        # # [:self.search_limit]
        # posts = title_posts.union(desc_posts)
        myposts = Post.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        return myposts

    def get_latest_posts(self):
        # posts = Post.objects.order_by('-created_at')[:10]
        pi = [6, 4, 12]
        postsid = Post.objects.filter(id__in=pi)
        return postsid


    def get_random_posts(self):
        post_ids = random.sample(list(Post.objects.values_list('id', flat=True)), k=self.random_limit)
        posts = Post.objects.filter(id__in=post_ids)
        return posts


    @classmethod
    def set_search_limit(cls, limit):
        """Método de classe para alterar o limite de resultados da busca."""
        cls.search_limit = limit






class ArtView(ListAPIView):


    list_arts =  [5]
    serializer_class = Postserializer
    queryset = Post.objects.filter(pk__in=(list_arts)).prefetch_related('favorites')
    # print(dir(queryset[0]))



class HighlightsView(ListAPIView):
    serializer_class = HighlightsSerializer
    queryset = HighlightsAdmin.objects.all().order_by('-pk')[:5]


# def search_view(request, term):
#     results = MyModel.objects.filter(name__icontains=term)
#     # Faz algo com os resultados da pesquisa
#     return render(request, 'search_results.html', {'results': results})


# def search_view(request):
#     search_term = request.GET.get('q')
#     results = MyModel.objects.filter(name__icontains=search_term)
#     # Faz algo com os resultados da pesquisa
#     return render(request, 'search_results.html', {'results': results})



# import re
#     ...:
#     ...: def query_to_words2(query):
#     ...:     # Remover os símbolos de pontuação e transformar em minúsculas
#     ...:     query = re.sub(r'[^\w\s+]', '', query).replace('+', ' ')
#     ...:     # Dividir a string em uma lista de palavras
#     ...:     words = query.split()
#     ...:     # Retornar a lista de palavras
#     ...:     return words
#     ...:
#  for i in range(0, len(lista)):
#         ...:     postsid.union(lista[i])


#  for query in fer:
#         ...:     myposts = Post.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
#     ...:     lista.append(myposts)


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


@csrf_exempt
def API_likes(request, pk):
    # serializer_class = LikeSerializer

    if request.method == 'POST':
        req = int((str(request.body))[-3])


        post = Post.objects.get(id=req)
        user = User.objects.get(id=request.user.id)
        like = Likes(User=user, Post=post )
        try:
            like.save()
            return HttpResponse(status=201)
        except Exception as e:
            if e.__class__.__name__ == 'IntegrityError':
                obj = user.likes_set.filter(Post_id=req)
                obj.delete()
                return HttpResponse(status=202)
            else:
                return HttpResponse(status=500)

    else:
        print(request.method)



        return Response({'serializer': {'ppppppppppppdsfsdf':'sdakdksalf fsdkfkse' }, 'Art': 'aos'})



    # def API_likes(request, pk):
    #     try:
    #     post = Post.objects.get(id=pk)
    # except Post.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    # user = User.objects.get(id=request.user.id)

    # like_data = {'User': user.id, 'Post': post.id}
    # like_serializer = LikeSerializer(data=like_data)

    # if like_serializer.is_valid():
    #     like_serializer.save()
    #     return Response(status=status.HTTP_201_CREATED)
    # else:
    #     if 'unique_together' in like_serializer.errors:
    #         existing_like = Likes.objects.filter(User=user, Post=post)
    #         existing_like.delete()
    #         return Response(status=status.HTTP_202_ACCEPTED)
    #     else:
    #         return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# @csrf_exempt
class like_api(CreateAPIView):
    serializer_class = LikeSerializer
    # queryset = Likes.objects.all()

    # def get_queryset(self):
    #     artid = self.kwargs.get('pk')
    #     # queryset = Comment.objects.filter(Post=(artid))
    #     queryset = Likes.objects.filter(Post=(artid))



    #     return queryset




@api_view(['GET'])
def search_view(request, q=None, genre=None,  rating=0):
    search_term = request.GET.get('q')
    print(search_term)
    posa=Posts_man().search_by_query(search_term)
    print(posa)
    # print(request.GET)
    # Faz algo com os resultados da pesquisa
    serializer = Postserializer(posa, many=True)
    print(dir(serializer))
    content = {'message': 'Hello, World!'}
    return Response(serializer.data)
# def search_view(request, q : str, genre : str,  rating : float = 0):




def hello_world(request):
    content = {'message': 'Hello, World!'}
    return Response(content)
