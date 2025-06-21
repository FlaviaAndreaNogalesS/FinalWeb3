from rest_framework import viewsets, permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from users.models import User
from users.permissions.is_superadmin import IsSuperAdmin
from users.serializers.user_serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self):
        if self.request.method != 'GET' and self.request.user.role != 'SUPERADMIN':
            self.permission_denied(self.request, message='Solo SUPERADMIN puede modificar usuarios')
        return super().get_permissions()

class UserListCreateView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsSuperAdmin]

# Obtener, actualizar o eliminar
class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsSuperAdmin]
    lookup_field = 'id'
