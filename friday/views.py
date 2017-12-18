import datetime
import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from friday import models


def index(request):
    context = {}
    context["cases"] = models.Case.objects.all()
    return render(request, "index.html", context)


@csrf_exempt
def case(request):
    response = models.Case.objects.get(name=json.loads(request.body.decode())['name'])
    return JsonResponse(str(response.json()), safe=False)


def hello(request):
    a1 = models.Activity.objects.create(name="Task 1", description="...",
                                        date=datetime.date(year=2017, month=12, day=14), time=datetime.time(), status=0,
                                        money=0)
    a1.people.add(models.Person.objects.get(pid=0))
    a2 = models.Activity.objects.create(name="Task 2", description="...",
                                        date=datetime.date(year=2017, month=12, day=14), time=datetime.time(), status=1,
                                        money=0)
    a2.people.add(models.Person.objects.get(pid=0))
    a3 = models.Activity.objects.create(name="Task 3", description="...",
                                        date=datetime.date(year=2017, month=12, day=14), time=datetime.time(), status=2,
                                        money=0)
    a3.people.add(models.Person.objects.get(pid=0))
    a4 = models.Activity.objects.create(name="Task 4", description="...",
                                        date=datetime.date(year=2017, month=12, day=14), time=datetime.time(), status=3,
                                        money=0)
    a4.people.add(models.Person.objects.get(pid=0))
    models.Case.objects.get(name="Weekly Tasks").activities.add(a1)
    models.Case.objects.get(name="Weekly Tasks").activities.add(a2)
    models.Case.objects.get(name="Weekly Tasks").activities.add(a3)
    models.Case.objects.get(name="Weekly Tasks").activities.add(a4)
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)
