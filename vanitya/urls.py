from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# Simple home route
def home_view(request):
    return JsonResponse({"message": "Welcome to the Vanitya API!"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),  # Home route for /
    path('api/auth/', include('authentication.urls')),
]
