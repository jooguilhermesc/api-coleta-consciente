from rest_framework import viewsets
from recycle.api import serializers
from recycle import models


class RecyleViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RecycleSerializers
    queryset = models.Recycle.objects.all()

