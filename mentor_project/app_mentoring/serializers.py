from rest_framework import serializers

from .models import *

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'is_active',
            'user_type',
        )
        read_only_fields = (
            'id',
        )


class NodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PioNode
        fields = '__all__'
        read_only_fields = (
            'id',
        )


class NodeUsersSerializer(serializers.ModelSerializer):
    users = serializers.SerializerMethodField()

    class Meta:
        model = PioNode
        fields = '__all__'
        read_only_fields = (
            'id',
        )
    
    def get_users(self, obj):
        qs = User.objects.filter(user_profile__node__id=obj.id)
        return UserSerializer(qs, many=True).data
