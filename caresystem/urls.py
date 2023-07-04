from django.urls import path

from caresystem.views import views as care_views

urlpatterns = [
    path('test/', care_views.test01)
]