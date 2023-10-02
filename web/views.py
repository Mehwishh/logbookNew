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
    if request.method == "POST":
        name = request.POST.get("name_of_invention")
        problem = request.POST.get("problem_it_solves")
        if record == None:
            recordOfInvention.objects.create(
                userId=pk,
                teamId=sk,
                name_of_invention=name,
                problem_it_solves=problem,
            )
            return redirect("statement_of_originality", pk, sk)
        if name != record.name_of_invention or problem != record.problem_it_solves:
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
    if request.method == "POST":
        return redirect("flowchart", pk, sk)
    return render(request, "website/statement_of_originality.html")


def flowchart(request, pk, sk):
    if request.method == "POST":
        return redirect("step_1", pk, sk)
    return render(request, "website/flowchart.html")


def step_1(request, pk, sk):
    step1 = stepOne.objects.filter(teamId=sk).order_by("-date_updated").first()
    print(step1)
    if request.method == "POST":
        identify_problems = request.POST.get("initial_problem")
        if step1 == None:
            stepOne.objects.create(
                userId=pk,
                teamId=sk,
                identify_problems=identify_problems,
            )
            return redirect("step_2", pk, sk)
        if identify_problems != step1.identify_problems:
            stepOne.objects.create(
                userId=pk,
                teamId=sk,
                identify_problems=identify_problems,
            )
            return redirect("step_2", pk, sk)
        return redirect("step_2", pk, sk)
    context = {"step1": step1}
    return render(request, "website/step_1.html", context)


def step_2(request, pk, sk):
    step2 = stepTwo.objects.filter(teamId=sk).order_by("-date_updated").first()
    print(step2)
    if request.method == "POST":
        p1name1 = request.POST.get("p1name1")
        p1name2 = request.POST.get("p1name2")
        p1name3 = request.POST.get("p1name3")
        p1name4 = request.POST.get("p1name4")
        p1age1 = request.POST.get("p1age1")
        p1age2 = request.POST.get("p1age2")
        p1age3 = request.POST.get("p1age3")
        p1age4 = request.POST.get("p1age4")
        p1comment1 = request.POST.get("p1comment1")
        p1comment2 = request.POST.get("p1comment2")
        p1comment3 = request.POST.get("p1comment3")
        p1comment4 = request.POST.get("p1comment4")

        p2name1 = request.POST.get("p2name1")
        p2name2 = request.POST.get("p2name2")
        p2name3 = request.POST.get("p2name3")
        p2name4 = request.POST.get("p2name4")
        p2age1 = request.POST.get("p2age1")
        p2age2 = request.POST.get("p2age2")
        p2age3 = request.POST.get("p2age3")
        p2age4 = request.POST.get("p2age4")
        p2comment1 = request.POST.get("p2comment1")
        p2comment2 = request.POST.get("p2comment2")
        p2comment3 = request.POST.get("p2comment3")
        p2comment4 = request.POST.get("p2comment4")

        p3name1 = request.POST.get("p3name1")
        p3name2 = request.POST.get("p3name2")
        p3name3 = request.POST.get("p3name3")
        p3name4 = request.POST.get("p3name4")
        p3age1 = request.POST.get("p3age1")
        p3age2 = request.POST.get("p3age2")
        p3age3 = request.POST.get("p3age3")
        p3age4 = request.POST.get("p3age4")
        p3comment1 = request.POST.get("p3comment1")
        p3comment2 = request.POST.get("p3comment2")
        p3comment3 = request.POST.get("p3comment3")
        p3comment4 = request.POST.get("p3comment4")

        p4name1 = request.POST.get("p4name1")
        p4name2 = request.POST.get("p4name2")
        p4name3 = request.POST.get("p4name3")
        p4name4 = request.POST.get("p4name4")
        p4age1 = request.POST.get("p4age1")
        p4age2 = request.POST.get("p4age2")
        p4age3 = request.POST.get("p4age3")
        p4age4 = request.POST.get("p4age4")
        p4comment1 = request.POST.get("p4comment1")
        p4comment2 = request.POST.get("p4comment2")
        p4comment3 = request.POST.get("p4comment3")
        p4comment4 = request.POST.get("p4comment4")

        other_notes = request.POST.get("other_notes")
        describe_problem = request.POST.get("describe_problem")
        specific_solution = request.POST.get("specific_solution")
        stepTwo.objects.create(
            userId=pk,
            teamId=sk,
            p1name1=p1name1,
            p1name2=p1name2,
            p1name3=p1name3,
            p1name4=p1name4,
            p1age1=p1age1,
            p1age2=p1age2,
            p1age3=p1age3,
            p1age4=p1age4,
            p1comment1=p1comment1,
            p1comment2=p1comment2,
            p1comment3=p1comment3,
            p1comment4=p1comment4,
            p2name1=p2name1,
            p2name2=p2name2,
            p2name3=p2name3,
            p2name4=p2name4,
            p2age1=p2age1,
            p2age2=p2age2,
            p2age3=p2age3,
            p2age4=p2age4,
            p2comment1=p2comment1,
            p2comment2=p2comment2,
            p2comment3=p2comment3,
            p2comment4=p2comment4,
            p3name1=p3name1,
            p3name2=p3name2,
            p3name3=p3name3,
            p3name4=p3name4,
            p3age1=p3age1,
            p3age2=p3age2,
            p3age3=p3age3,
            p3age4=p3age4,
            p3comment1=p3comment1,
            p3comment2=p3comment2,
            p3comment3=p3comment3,
            p3comment4=p3comment4,
            p4name1=p4name1,
            p4name2=p4name2,
            p4name3=p4name3,
            p4name4=p4name4,
            p4age1=p4age1,
            p4age2=p4age2,
            p4age3=p4age3,
            p4age4=p4age4,
            p4comment1=p4comment1,
            p4comment2=p4comment2,
            p4comment3=p4comment3,
            p4comment4=p4comment4,
            other_notes=other_notes,
            describe_problem=describe_problem,
            specific_solution=specific_solution,
        )
        return redirect("step_3", pk, sk)
    context = {"step2": step2}
    return render(request, "website/step_2.html", context)


def step_3(request, pk, sk):
    step3 = stepThree.objects.filter(teamId=sk).order_by("-date_updated").first()
    if request.method == "POST":
        factors = request.POST.get("factors")
        ways_to_solve = request.POST.get("ways_to_solve")
        research = request.POST.get("research")
        difference = request.POST.get("difference")
        if step3 == None:
            stepThree.objects.create(
                userId=pk,
                teamId=sk,
                factors=factors,
            )
            return redirect("step_4", pk, sk)
        elif (
            factors != step3.factors
            or ways_to_solve != step3.ways_to_solve
            or research != step3.research
            or difference != step3.difference
        ):
            stepThree.objects.create(
                userId=pk,
                teamId=sk,
                factors=factors,
                ways_to_solve=ways_to_solve,
                research=research,
                difference=difference,
            )
            return redirect("step_4", pk, sk)
        return redirect("step_4", pk, sk)
    context = {"step3": step3}
    return render(request, "website/step_3.html", context)


def step_4(request, pk, sk):
    step4 = stepFour.objects.filter(teamId=sk).order_by("-date_updated").first()
    if request.method == "POST":
        blueprint = request.POST.get("blueprint")
        teacher_name = request.POST.get("teacher_name")
        teacher_sign = request.POST.get("teacher_sign")
        date = request.POST.get("date")
        i1expert = request.POST.get("i1expert")
        i1credentials = request.POST.get("i1credentials")
        i1identified = request.POST.get("i1identified")
        i1problemface = request.POST.get("i1problemface")
        i2expert = request.POST.get("i2expert")
        i2credentials = request.POST.get("i2credentials")
        i2identified = request.POST.get("i2identified")
        i2problemface = request.POST.get("i2problemface")
        i3expert = request.POST.get("i3expert")
        i3credentials = request.POST.get("i3credentials")
        i3identified = request.POST.get("i3identified")
        i3problemface = request.POST.get("i3problemface")
        sol_design_problem = request.POST.get("sol_design_problem")
        green_sol = request.POST.get("green_sol")
        stepFour.objects.create(
            userId=pk,
            teamId=sk,
            blueprint=blueprint,
            teacher_name=teacher_name,
            teacher_sign=teacher_sign,
            date=date,
            i1expert=i1expert,
            i1credentials=i1credentials,
            i1identified=i1identified,
            i1problemface=i1problemface,
            i2expert=i2expert,
            i2credentials=i2credentials,
            i2identified=i2identified,
            i2problemface=i2problemface,
            i3expert=i3expert,
            i3credentials=i3credentials,
            i3identified=i3identified,
            i3problemface=i3problemface,
            sol_design_problem=sol_design_problem,
            green_sol=green_sol,
        )
        return redirect("step_5", pk, sk)
    context = {"step4": step4}
    return render(request, "website/step_4.html", context)


def step_5(request, pk, sk):
    step5 = stepFive.objects.filter(teamId=sk).order_by("-date_updated").first()
    if request.method == "POST":
        materials = request.POST.get("materials")
        findings = request.POST.get("findings")
        credit = request.POST.get("credit")
        if step5 == None:
            stepFive.objects.create(
                userId=pk,
                teamId=sk,
                materials=materials,
                findings=findings,
                credit=credit,
            )
            return redirect("step_6", pk, sk)
        elif (
            materials != step5.materials
            or findings != step5.findings
            or credit != step5.credit
        ):
            stepFive.objects.create(
                userId=pk,
                teamId=sk,
                materials=materials,
                findings=findings,
                credit=credit,
            )
            return redirect("step_6", pk, sk)
        return redirect("step_6", pk, sk)
    context = {"step5": step5}
    return render(request, "website/step_5.html", context)


def step_6(request, pk, sk):
    step6 = stepSix.objects.filter(teamId=sk).order_by("-date_updated").first()
    if request.method == "POST":
        notes = request.POST.get("notes")
        prototype_pic = request.POST.get("prototype_pic")
        if step6 == None:
            stepSix.objects.create(
                userId=pk,
                teamId=sk,
                notes=notes,
                prototype_pic=prototype_pic,
            )
            return redirect("step_6", pk, sk)
        elif notes != step6.notes or prototype_pic != step6.prototype_pic:
            stepSix.objects.create(
                userId=pk,
                teamId=sk,
                notes=notes,
                prototype_pic=prototype_pic,
            )
            return redirect("step_7", pk, sk)
        return redirect("step_7", pk, sk)
    context = {"step6": step6}
    return render(request, "website/step_6.html", context)


def step_7(request, pk, sk):
    return render(request, "website/step_7.html")


def step_8(request, pk, sk):
    return render(request, "website/step_8.html")


def survey(request, pk, sk):
    return HttpResponse("survey")


def notes(request, pk, sk):
    return HttpResponse("notes")


def preview_logbook(request, pk, sk):
    return HttpResponse("preview_logbook")
