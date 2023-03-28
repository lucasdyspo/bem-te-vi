from rest_framework import serializers
# from bemtevi.serializers import DynamicFieldsModelSerializer
# from home.serializer import Artsfeedserializer
# from login.serializers  import UserSerializer
from .models import Post, HighlightsAdmin, Likes, Comment
from common.serializer  import DynamicFieldsModelSerializer
from users.serializers import UserSerializer
from rest_framework import serializers
from django.utils.text import slugify


# class LikeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Likes
#         ordering = ['created_at', 'pk']
#         fields = '__all__'
#         unique_together = ['art', 'user']



# class UserSerializer(DynamicFieldsModelSerializer):
#     ...

# class Commentsserializer(serializers.ModelSerializer):
#     # user = UserSerializer(many=True, fields=['vulgo', 'nome', 'id', 'pathphoto',])
#     # art = serializers.CharField(max_length=100, read_only=True)

#     class Meta:
#         model = Comment
#         fields = '__all__'


class Postserializer(DynamicFieldsModelSerializer):
    author = UserSerializer(many=False, fields=['username', 'name', 'id', 'img'])
    collaborators = UserSerializer(many=True, fields=['username', 'id', 'img'], required=False)
    slug = serializers.SlugField(source='title',)

    likes = serializers.IntegerField(source='likes.count',)

    class Meta:
        model = Post
        exclude = ['createdAt', 'updatedAt']










# class Pageserializer(Artserializer,Commentsserializer, ):
#     ...


class HighlightsSerializer(serializers.ModelSerializer):

    class Meta:
        model = HighlightsAdmin
        fields = '__all__'






class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        ordering = ['created_at', 'pk']
        fields = '__all__'



class Commentsserializer(serializers.ModelSerializer):
    user = UserSerializer(many=True, fields=['vulgo', 'nome', 'id', 'img',])
    post = serializers.CharField(max_length=100, read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'




