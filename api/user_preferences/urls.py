from django.urls import path
from user_preferences import views

urlpatterns = [
    path('user_prefs/', views.UserPrefList.as_view()),
    path('user_prefs/id/<int:pk>/', views.UserPrefItem.as_view()),
    path('user_prefs/user/<int:userId>/', views.UserPrefItemByUser.as_view()),
    path('session', views.CheckSessionView.as_view())
]