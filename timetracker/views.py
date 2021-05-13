from rest_framework.views import APIView

from .models import TimeTrackRecord, StartEndTimeRecord
from .serializers import TimeTrackRecordSerializer, StartEndTimeRecordSerializer
from rest_framework.response import Response
from rest_framework import permissions, generics, status

from django.utils import timezone

class TimeTrackRecordListApiView(generics.ListCreateAPIView):
    def get_queryset(self):
        user = self.request.user
        return TimeTrackRecord.objects.filter(user = user)
    
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TimeTrackRecordSerializer


class TimeTrackRecordActions(APIView):
    def post(self, request, id, *args, **kwargs):
        action = request.GET.get('action','start')
        try:
            timetrackrecord_obj = TimeTrackRecord.objects.get(id = id)
        except:
            return Response('object did not found', status.HTTP_404_NOT_FOUND)

        if action == 'start':
            start_end_record = StartEndTimeRecord.objects.create(
                user = request.user
            )
            start_end_record.save()
            timetrackrecord_obj.start_end_records.add(start_end_record)
            return Response({'start_end_record_id':start_end_record.id})

        if action == 'stop':
            record_id = request.GET.get('record_id',None)
            try:
                startendrecord_obj = StartEndTimeRecord.objects.get(id = record_id)
            except:
                return Response('object did not found', status.HTTP_404_NOT_FOUND)
            
            startendrecord_obj.end_time = timezone.now()
            startendrecord_obj.get_second()
            startendrecord_obj.save()
            return Response('item stopped')
            

