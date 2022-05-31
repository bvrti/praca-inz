from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('report-malfunction/', views.reportMalfunction, name='reportMalfunction'),
    path('report-malfunction/success/', views.reportMalfunctionSuccess, name='reportMalfunctionSuccess'),
    path('reports-opened-malfunctions/', views.reportsopenedmalfunctions, name='reports-opened-malfunctions'),
    path('view-malfunction/<int:id>', views.viewMalfunction, name='view-malfunction'),
]
