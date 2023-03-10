from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import viewsets

from .serializers import RegisterSerializer, UserSerializer
from .models import User
# Register 
class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    
    def post(self, request, *args, **kwargs):
        serializer: RegisterSerializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=False)
    
        if serializer.errors:
            err_str = ""
            for error_list in serializer.errors.values():
                for err in error_list:
                    err_str += err.title() + " "
            
            return Response({
                'detail': err_str
            }, status=status.HTTP_406_NOT_ACCEPTABLE)

        user = serializer.save()

        return Response({
            "message": "Nutzer erstellt. Der Nutzer kann sich nun einloggen."
        })

class UserViewSet(
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer