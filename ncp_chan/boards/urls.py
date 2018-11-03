from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('wel/', views.wel, name="b-wel")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
