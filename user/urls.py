from django.urls import path
from django.contrib.auth import views as auth_views
from user.views import OwnLoginView, OwnLogoutView, SignupView, ProfileView


urlpatterns = [
    path('login/', OwnLoginView.as_view(), name='login'),  
    path('logout/', OwnLogoutView.as_view(), name='logout'),

    path('signup/', SignupView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name = 'user/password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name = 'user/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'user/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'user/password_reset_complete.html'), name='password_reset_complete'),
]
