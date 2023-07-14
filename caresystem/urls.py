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
    path('getViolenceStream/', care_views.getViolenceStream),
    path('getEmotionList/', care_views.getEmotionList),
    path('getIntrusionList/', care_views.getIntrusionList),
    path('getFallList/', care_views.getFallList),
    path('getInteractList/', care_views.getInteractList),
    # path('areaChoose/', care_views.areaChoose), # 入侵区域选择
    path('getIntrusionStream/', care_views.getIntrusionStream),  # 入侵检测

]