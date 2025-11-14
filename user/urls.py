from django.urls import path
from django.contrib.auth import views as auth_views
from user.views import OwnLoginView, SignupView, ProfileView

urlpatterns = [
    path('login/', OwnLoginView.as_view(), name='login'),  
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('signup/', SignupView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
