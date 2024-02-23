from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('userlogin', views.userlogin, name="userlogin"),
    path('useregister', views.useregister, name="useregister"),
    path('uploadfiles', views.uploadfiles, name="uploadfiles"),
    path('myfiles', views.myfiles, name="myfiles"),
    path('auditfile', views.auditfile, name="auditfile"),
    path('auditmyfiles/<int:id>/<str:filename>',
         views.auditmyfiles, name="auditmyfiles"),
    path('audittransactions', views.audittransactions, name="audittransactions"),
    path('deletefile/<int:id>',views.deletefile,name="deletefile")

]
