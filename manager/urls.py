from django.urls import path
from manager import views

urlpatterns = [
    path('',views.home),
    path('register/',views.newAdmission),
    path('staff/',views.staffLogin),
    path('about/',views.showAbout),
    path('dashboard/',views.dashboard),
    path('feestruct/',views.showfeestruct),
    path('logout/',views.logoutUser),
    path('dashboard/students/',views.showStudentsList),
    path('dashboard/applications/',views.showApplicationsList),
    path('dashboard/staff/',views.showStaffList),
    path('remove/student/<str:adm>',views.removeStudent),
    path('remove/employee/<str:id>',views.removeEmployee),
    path('approve/<str:appid>',views.approveApplication),
]