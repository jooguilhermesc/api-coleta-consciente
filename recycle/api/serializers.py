from rest_framework import serializers
from recycle import models


class RecycleSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Recycle
        fields = '__all__'
