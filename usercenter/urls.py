from django.urls import path

from usercenter.views import views as user_views

urlpatterns = [
    path('login/', user_views.userLogin),
    path('changePW/', user_views.changePw),
    path('changeInfo/', user_views.changeUserInfo),
    path('addNewUser/', user_views.addNewUser),
    path('getuser/', user_views.getuser),
    path('getUserNum/', user_views.getUserNum)
]