from django.urls import path
from authentication.views import RegisterView, LoginView, ProfileView, ProfileUpdateView, LogoutView, LanguagePreferenceView


urlpatterns = [
    path('signup/', RegisterView.as_view(), name='signup'),
    path('signin/', LoginView.as_view(), name='signin'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='profile-edit'),
    path('logout/', LogoutView.as_view(), name='logout'),
   path('language-preference/', LanguagePreferenceView.as_view(), name='language-preference'),
   path('preference/', LanguagePreferenceView.as_view(), name='preference'),
]
