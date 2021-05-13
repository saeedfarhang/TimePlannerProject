from rest_framework import serializers
from .models import TimeTrackRecord, StartEndTimeRecord

from datetime import datetime

class StartEndTimeRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = StartEndTimeRecord
        fields = ['start_time', 'end_time']


class TimeTrackRecordSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = TimeTrackRecord
        fields = [
            'id',
            'user',
            'timeinsecond',
            'title',
        ]
    
    def create(self, validated_data):
        record_obj = TimeTrackRecord(
            title = validated_data.get('title'),
            user = self.context['request'].user
        )
        record_obj.save()
        return record_obj

