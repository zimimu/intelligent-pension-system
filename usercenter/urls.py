from django.urls import path

from usercenter.views import views as user_views

urlpatterns = [
    path('test/', user_views.test01)
]