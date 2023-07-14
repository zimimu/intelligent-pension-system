from django.urls import path

from caresystem.views import views as care_views

urlpatterns = [
    path('test/', care_views.test01),
    path('getEventList/', care_views.getEventInfo),
    path('getFacialExpressionStream/', care_views.getFacialExpressionStream),
    path('getFalldetectionStream/', care_views.getFenceinStream),
    path('getFenceinStream/', care_views.getFenceinStream),
    path('getVolunteeractStream/', care_views.getVolunteeractStream),
    path('getEmotionList/', care_views.getEmotionList),
    path('getIntrusionList/', care_views.getIntrusionList),
    path('getFallList/', care_views.getFallList),
    path('getInteractList/', care_views.getInteractList),
    path('changeEventStatus/', care_views.changeEventStatus),
    path('getChatContent/', care_views.getChatResult),
    path('addNewCall/', care_views.addCallEvent)
]