
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("",views.index,name="shopname"),
    path("aboutus/",views.about,name="about"),
    path("contact/",views.contact,name="contact"),
    path("tracker/",views.tracker,name="trackingstatus"),
    path("search/",views.search,name="search"),
    path("product/<int:myid>",views.product,name="product"),
    path("checkout/",views.checkout,name="checkout"),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),
]
