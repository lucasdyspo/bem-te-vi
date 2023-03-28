from common.serializer  import DynamicFieldsModelSerializer
from .models import User
from rest_framework import serializers


class UserSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = User
        exclude = ['password', 'last_login', "created", "modified", "updatedAt"]




class ProfileSerializer(UserSerializer):

    # friends = UserSerializer(many=True, fields=['vulgo', 'nome', 'id', 'pathphoto',])
    # user_main =
    friends = serializers.IntegerField(source='friends.count',)
    arts_realizatas = serializers.IntegerField(source='user_author.count',)
    users_collaborators = serializers.IntegerField(source='users_collab.count')

