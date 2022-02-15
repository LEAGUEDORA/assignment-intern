from .views import classAvgGenderHeightView, classAvgheightView, classRegInFeb, classSecAvgHeiWei
from django.urls import path

urlpatterns = [
    path("clsavggenderheight", classAvgGenderHeightView),
    path("clsavgheight", classAvgheightView),
    path("clsreg", classRegInFeb),
    path("clssecavgheiwei", classSecAvgHeiWei)
]