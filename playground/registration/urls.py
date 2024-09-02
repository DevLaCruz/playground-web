from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView, ProfileUpdate, EmailUpdate
from django.conf import settings

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    # Asegúrate de que esta línea está presente
    path('profile/', ProfileUpdate.as_view(), name='profile'),
    path('profile/email', EmailUpdate.as_view(), name='profile_email'),

]
