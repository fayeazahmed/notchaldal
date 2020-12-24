from django.urls import path
from .views import SignInView, SignupView, GetUserView, ProfileView

urlpatterns = [
    path('signinorup', SignInView.as_view()),
    path('signup', SignupView.as_view()),
    path('profile', ProfileView.as_view()),
    path('<id>', GetUserView.as_view())
]
