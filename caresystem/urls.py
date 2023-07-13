from django.urls import path

from caresystem.views import views as care_views

urlpatterns = [
    path('test/', care_views.test01),
    path('getEventList/', care_views.getEventInfo),
    path('getFacialExpressionStream/',care_views.getFacialExpressionStream),
    path('getFalldetectionStream/',care_views.getFalldetectionStream),
    path('getFenceinStream/', care_views.getFenceinStream),
    path('getVolunteeractStream/', care_views.getVolunteeractStream),
    path('getFiredetectionStream/', care_views.getFiredetectionStream),
    path('getViolenceStream/', care_views.getViolenceStream)

]