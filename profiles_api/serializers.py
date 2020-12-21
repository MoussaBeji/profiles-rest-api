from rest_framework import serializers
from .models import UserProfile

#class HellowSerialiser(serializers.Serializer):
#    """ Serializes a name field fro apiview"""
#    name = serializers.CharField(max_length=10)




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'password'
                  )
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """create new user"""
        user = UserProfile.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password']
        )

        return user
