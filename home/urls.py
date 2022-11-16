
from django.urls import path
from .views import PostCargo,GetHistory,AllVehicleCategory,AllUserPrice,CargoTrack,CurrentLocationApi

urlpatterns = [

    path("add/cargo/",PostCargo.as_view()),
    path("update/cargo/",GetHistory.as_view()),
    path("all/category/",AllVehicleCategory.as_view()),
    path("all/price/",AllUserPrice.as_view()),
    path("track/cargo/",CargoTrack.as_view()),
    path("save/currentlocation/",CurrentLocationApi.as_view())
  
]
