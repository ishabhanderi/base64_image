
from rest_framework import serializers
from .models import File,Image
from drf_extra_fields.fields import Base64ImageField

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'


    
class ImageSerializer(serializers.ModelSerializer):
    image=Base64ImageField()

    class Meta:
        model = Image
        fields = ['image']


class ImageRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ['image']