from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Resume
from .serializers import ResumeSerializer
from .permissions import IsCandidate, IsHR, IsAdmin, IsOwnerOrAdmin

class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['owner']

    def get_queryset(self):
        user = self.request.user
        if user.role == 'ADMIN':
            return self.queryset
        elif user.role == 'HR':
            return self.queryset
        return self.queryset.filter(owner=user)

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated, IsCandidate]
        elif self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)