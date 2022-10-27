from rest_framework import serializers
from .models import SlackDetail

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlackDetail
        fields = ['slackUsername', 'backend', 'age', 'bio']