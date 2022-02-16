from rest_framework import serializers
from apps.test_service.models import Test, FioTestConfig

class TestSerializer(serializers.HyperlinkedModelSerializer):
    """
    Contains a serializer for Test objects. Serializes all fields based
    on the model serializer provided by Django. 

    """
    
    
    class Meta:
        model = Test
        fields = '__all__'


