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
    path('remove/<str:admNum>',views.removeStudent),
    path('approve/<str:appid>',views.approveApplication),
]