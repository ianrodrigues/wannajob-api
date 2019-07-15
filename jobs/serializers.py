from rest_framework import serializers

from .models import Job


class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = ('id', 'title', 'seniority_level', 'salary', 'city', 'country')
