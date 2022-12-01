from django.urls import path
from user_preferences import views

urlpatterns = [
    path('user_prefs/', views.UserPrefList.as_view()),
    path('user_prefs/<int:pk>/', views.UserPrefItem.as_view())
]