from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.job_list),
    path("<int:pk>/", views.job_detail),
]
