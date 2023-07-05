from django.urls.conf import path
from dropdown import views
app_name='dropdown'
urlpatterns = [
    path('',views.index,name="index"),
    path('getdata/', views.getdata, name="getdata"),
]