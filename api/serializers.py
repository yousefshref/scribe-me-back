from rest_framework import serializers

from . import models

class ImageDescriptionSerializer(serializers.Serializer):
    image = serializers.CharField()  # base64-encoded image
    language = serializers.ChoiceField(choices=["English", "Arabic", "Spanish"], default="English")


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.History
        fields = "__all__"





