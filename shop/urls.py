from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path('login/',views.login_view,name="login"),
    path('register/',views.register_view,name="register"),
    path('logout/',views.logout_view,name="logout"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contactus"),
    path('search/',views.search,name="search"),
    path('tracker/',views.tracker,name="tracker"),
    path('checkout/',views.checkout,name="checkout"),
    path('cart/',views.cart,name="cart"),
    path('productview/<int:id>',views.productview,name="prodview")
]
