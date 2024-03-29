from django.urls import path, include
from . import views

app_name='jobs'

urlpatterns = [
    path("", views.job_list),
    path("<int:pk>/", views.job_detail, name="job_detail"),
]
