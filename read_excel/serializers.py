from rest_framework import serializers
from .models import *

class IapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Iap
        fields = '__all__'
