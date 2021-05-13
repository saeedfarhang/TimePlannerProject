from django.urls import path
from .views import TimeTrackRecordListApiView, TimeTrackRecordActions

urlpatterns = [
    path('', TimeTrackRecordListApiView.as_view() ,name=''),
    path('<id>/', TimeTrackRecordActions.as_view() ,name='time_track_record_action'),

]