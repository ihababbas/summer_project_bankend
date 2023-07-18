from rest_framework import serializers
from .models import QuestionsData

class QuestionsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionsData
        fields = ['id', 'type', 'questions','correct','wrong1','wrong2','wrong3']