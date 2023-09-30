from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import *


def index(request):
    return render(request, "website/index.html")


def course_outline(request, pk, sk):
    return render(request, "website/outline.html")


def record_of_invention(request, pk, sk):
    record = (
        recordOfInvention.objects.filter(teamId=sk).order_by("-date_updated").first()
    )
    print(record.name_of_invention, record.problem_it_solves)
    if request.method == "POST":
        name = request.POST.get("name_of_invention")
        problem = request.POST.get("problem_it_solves")
        if (
            name != record.name_of_invention
            and problem != record.problem_it_solves
        ):
            recordOfInvention.objects.create(
                userId=pk,
                teamId=sk,
                name_of_invention=name,
                problem_it_solves=problem,
            )
            return redirect("statement_of_originality", pk, sk)
        return redirect("statement_of_originality", pk, sk)
    context = {"record": record}
    return render(request, "website/record_of_invention.html", context)


def statement_of_originality(request, pk, sk):
    return render(request, "website/statement_of_originality.html")


def flowchart(request, pk, sk):
    return render(request, "website/flowchart.html")


def step_1(request, pk, sk):
    return render(request, "website/step_1.html")


def step_2(request, pk, sk):
    return HttpResponse("step_2")


def step_3(request, pk, sk):
    return HttpResponse("step_3")


def step_4(request, pk, sk):
    return HttpResponse("step_4")


def step_5(request, pk, sk):
    return HttpResponse("step_5")


def step_6(request, pk, sk):
    return HttpResponse("step_6")


def step_7(request, pk, sk):
    return HttpResponse("step_7")


def step_8(request, pk, sk):
    return HttpResponse("step_8")


def survey(request, pk, sk):
    return HttpResponse("survey")


def notes(request, pk, sk):
    return HttpResponse("notes")


def preview_logbook(request, pk, sk):
    return HttpResponse("preview_logbook")
