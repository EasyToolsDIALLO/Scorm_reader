from .models import *
from rest_framework import serializers


##################################### OCR############################################


class ScormFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyScormModel
        fields = ['id', 'file']