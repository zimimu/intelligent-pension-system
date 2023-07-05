from django.urls import path

from usercenter.views import views as user_views

urlpatterns = [
    path('test/', user_views.test01),
    path('login/', user_views.userLogin),
    path('changePW/', user_views.changePw),
    path('changeInfo/', user_views.changeUserInfo),
    path('addNewUser/', user_views.addNewUser)
]