from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('report-malfunction/', views.reportMalfunction, name='reportMalfunction'),
    path('test', views.test, name='test'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
