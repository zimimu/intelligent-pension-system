from django.urls import path

from managementcenter.views import views as manage_views

urlpatterns = [
    path('test/', manage_views.test03)
]