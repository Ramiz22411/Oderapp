from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexPage.as_view(), name="index"),
    path("ads-list/", views.AdsList.as_view(), name="ads-list"),
    path('ads-create/', views.AdsCreate.as_view(), name="ads-create"),
    path("ads-update", views.AdsUpdate.as_view(), name="ads-update"),
    path('ads-detail/<int:pk>/', views.AdsDetail.as_view(), name="ads-detail"),
    path('ads-delete/<int:pk>/', views.AdsDelete.as_view(), name="ads-delete"),
    path('my-ads/', views.MyadsList.as_view(), name="my-ads"),
    path('exchange-offers/', views.ExchangeOfferList.as_view(), name="exchange-offers")
]
