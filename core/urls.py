

from django.contrib import admin
from django.urls import include, path
from .views import index,profile,events_page
from django.conf import settings
from django.conf.urls.static import static

app_name = "core"
urlpatterns = [
    path('index/',index, name="index" ),  # Include your app's URLs
    path('profile/',profile, name="profile"),
    path('eventspage/<int:event_id>/', events_page, name="eventspage"),  # Corrected URL pattern
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

