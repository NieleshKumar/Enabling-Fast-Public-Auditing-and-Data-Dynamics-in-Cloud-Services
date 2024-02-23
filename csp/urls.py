from django.urls import path
from . import views

urlpatterns = [
    path('csp', views.csp, name="csp"),
    path('useractivation', views.useractivation, name="useractivation"),
    path('activeuser/<int:id>', views.activeuser, name="activeuser"),
    path('userdetails', views.userdetails, name="userdetails"),
    path('cloudfiles', views.cloudfiles, name="cloudfiles"),
    path('auditrequests', views.auditrequests, name="auditrequests"),
    path('generateproof/<int:id>', views.generateproof, name="generateproof"),
    path('editfile/<str:id>/<str:filename>', views.editfile, name='editfile'),
    path('updatecontent', views.updatecontent, name="updatecontent"),


]
