#from rest_framework.authtoken.views import ObtainAuthToken
#from rest_framework.authtoken.models import Token

from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework import permissions, status
from django.contrib.auth.models import User
from .serializers import UsersSerializer, RegisterSerializer

'''class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
'''
class RegisterView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        

                
          

class UserList(APIView):

    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            model = Users.objects.get(id=id)
            serializer = UsersSerializer(model)
            return Response(serializer.data)

        model = Users.objects.all()
        serializer = UsersSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    def put(self, request, pk, format=None):
        id = pk
        model = Users.objects.get(id=id)
        serializer = UsersSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, pk, format=None):
        id = pk
        model = Users.objects.get(id=id)
        serializer = UsersSerializer(model, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        id = pk
        model = Users.objects.get(id=id)
        model.delete()
        return Response({'msg':'Data deleted'})
