from django.urls import path
from . import views

urlpatterns = [
    path('tpa', views.tpa, name="tpa"),
    path('users', views.users, name="users"),
    path('integrity', views.integrity, name="integrity"),
    path('viewmetadata/<int:fileid>', views.viewmetadata, name="viewmetadata"),
    path('challengecloud/<int:id>', views.challengecloud, name="challengecloud"),
    path('challengestatus', views.challengestatus, name="challengestatus"),
    path('checkuser/<int:fileid>', views.checkuser, name="checkuser"),
    path('allaudits', views.allaudits, name="allaudits"),




]
