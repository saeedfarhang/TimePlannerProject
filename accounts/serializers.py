from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email',
            'name'
        ]
    

class UserRegisterSerializer(serializers.ModelSerializer):
    password        = serializers.CharField(write_only=True)
    password2       = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = [
            'email',
            'name',
            'password',
            'password2'
        ]
    # extra_kwargs= 
    def validate(self, data):
        pw = data.get('password')
        pw2 = data.pop('password2')

        if pw != pw2:
            raise serializers.ValidationError('passwords are not match!')
        return data

    def create(self, validated_data):
        user_obj = User(
            email = validated_data.get('email'),
            name = validated_data.get('name')
        )
        user_obj.set_password(validated_data.get('password'))
        user_obj.save()
        return user_obj