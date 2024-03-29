from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('listing/<str:pk>/', views.listing, name="listing"),
    path('create-listing/', views.createListing, name="create-listing"),
    path('update-listing/<str:pk>', views.updateListing, name="update-listing"),
    path('delete-listing/<str:pk>', views.deleteListing, name="delete-listing"),
    path('claim/<str:pk>/', views.claim, name="claim"),
]
