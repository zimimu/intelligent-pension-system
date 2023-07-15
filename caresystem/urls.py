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
    path('getIntrusionList/', care_views.getIntrusionList), # 入侵
    path('getFallList/', care_views.getFallList),
    path('getInteractList/', care_views.getInteractList), # 交互
    path('getFireList/',care_views.getFireList),# 火焰
    path('getViolenceList/',care_views.getViolenceList),# 暴力

    # path('areaChoose/', care_views.areaChoose), # 入侵区域选择
    path('getIntrusionStream/', care_views.getIntrusionStream),  # 入侵检测


    path('getInteractList/', care_views.getInteractList),
    path('changeEventStatus/', care_views.changeEventStatus),
    path('getChatContent/', care_views.getChatResult),
    path('addNewCall/', care_views.addCallEvent),

]