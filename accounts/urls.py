from django.urls import path
from . import views

urlpatterns = [
    path('', views.registerVendorPage, name='index'),
    path('registerbidder/', views.registerBidderPage, name='registerbidder'),
    path('login/', views.loginpage, name='contact'),
    path('home', views.home, name='home'),
    path('vendor/', views.VendorList.as_view()),
    path('bidder/', views.BidderList.as_view()),

]