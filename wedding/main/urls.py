from django.urls import path
from . import views

urlpatterns=[
    path("", views.main, name="main"),
    path('band/<int:band_id>/<str:date>/', views.check_band_availability, name="check_band_availability"),
    path('band/', views.band, name = "band"),
    path('cake/', views.cake, name = "cake"),
    path('photographer/',views.photographer,name="photographer"),
    path('dress/',views.dress,name="dress"),
    path('flower/',views.flower,name="flower"),
    path('image/', views.band, name = "band"),
    path('venue/', views.venue, name = "venue"),
]