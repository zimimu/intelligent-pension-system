from django.urls import path

from managementcenter.views import views as manage_views

urlpatterns = [
    path('test/',manage_views.test),
    path('addOld/', manage_views.addOldInfo),
    path('updateOld/', manage_views.updateOldInfo),
    path('checkoutOld/', manage_views.checkoutOld),
    path('checkOldById/', manage_views.checkOldById),
    path('getOldList/', manage_views.getOldList),
    path('addEmployee/', manage_views.addEmployeeInfo),
    path('updateEmployee/', manage_views.updateEmployeeInfo),
    path('resignEmployee/', manage_views.resignTmployee),
    path('checkEmployeeById/', manage_views.checkEmployeeById),
    path('getEmployeeList/', manage_views.getEmployeeList),
    path('addVolunteer/', manage_views.addVolunteerInfo),
    path('updateVolunteer/', manage_views.updateVolunteerInfo),
    path('checkoutVolunteer/', manage_views.checkoutVolunteer),
    path('checkVolunteerById/', manage_views.checkVolunteerById),
    path('getVolunteerList/', manage_views.getVolunteerList),
    path('getGuartionPhone/', manage_views.getGuartionPhone),
    path('getFaceCollectionStream/', manage_views.getFaceCollectionStream),
    path('getOldAgeNum/', manage_views.getOldAgeNum),
    path('getOldNum/', manage_views.getOldNum),
    path('getVolunteerNum/', manage_views.getVolunteerNum),
    path('getEmployeeNum/', manage_views.getEmployeeNum)
]