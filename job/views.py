from django.shortcuts import render
from .models import Job, Category


def job_list(request, *args, **kwargs):
    queryset = list(Job.objects.all())
    context = {
        "jobs": queryset,
        "number_of_jobs": len(queryset),
    }
    return render(request, "job/job_list.html", context)


def job_detail(request, *args, **kwargs):
    try:
        job = Job.objects.get(pk=kwargs["pk"])
        context = {"job": job}
    except Job.DoesNotExist:
        context = {"job": "NOT FOUND"}

    return render(request, "job/job_detail.html", context)
