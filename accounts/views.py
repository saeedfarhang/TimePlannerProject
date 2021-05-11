from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.mixins import RetrieveModelMixin, DestroyModelMixin
from rest_framework import permissions
from rest_framework.response import Response
from .serializers import UserRegisterSerializer, UserSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

class CreateUserApiView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserRegisterSerializer

class UserApiView(RetrieveModelMixin,DestroyModelMixin,UpdateAPIView):
    queryset = User.objects.all()
    permission_classes= [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = UserSerializer
    lookup_field = 'id'
    def put(self, request, id, *args, **kwargs):
        if request.user != self.queryset.get(id = id):
            return Response('you can not change other users data')
        return self.update(request, *args, **kwargs)
        
    def get(self, request, id ,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)
    
    def delete(self, request, id, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)