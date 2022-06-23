from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),

    path('view-malfunction/<int:id>', views.viewMalfunction, name='view-malfunction'),

    path('report-malfunction/', include ([
        path('', views.reportMalfunction, name='reportMalfunction'),
        path('success', views.reportMalfunctionSuccess, name='reportMalfunctionSuccess'),
    ])),

    path('reports/', include ([
        path('', views.reports, name='reports'),
        path('opened-malfunctions', views.reportsopenedmalfunctions, name='reports-opened-malfunctions'),
    ]))
]
