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





def search_view(request, q, genre=None,  rating=0):
    search_term = request.GET.get('q')
    print(dir(request.GET))
    print(request.GET)
    # Faz algo com os resultados da pesquisa
    return HttpResponse(status=404)
# def search_view(request, q : str, genre : str,  rating : float = 0):

