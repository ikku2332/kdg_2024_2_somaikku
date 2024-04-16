from django.urls import path
from . import views

urlpatterns = [
    path('mayopanintroduction', views.ListMayopanintroductionView.as_view(), name='mayopanintroduction'),
    path('mayopansynopsis', views.ListMayopansynopsisView.as_view(), name='mayopansynopsis'),
    path('mayopancharacter', views.ListMayopancharacterView.as_view(), name='mayopancharacter'),
]