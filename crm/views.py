import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from crm import models


@csrf_exempt
def index(request):
    context = {}
    if request.GET.get("page") == "" or request.GET.get("page") is None:
        context["main"] = "Home"
        context["page"] = "newClient"
    else:
        context["main"] = request.GET.get("main")
        context["page"] = request.GET.get("page")
    return render(request, 'index.html', context)


def create_client_form(request):
    success = True
    context = {}
    context["content"] = ""
    if len(models.Company.objects.filter(name=request.POST.get("client_name"))) > 0:
        success = False
        context["content"] += "Name {} already exist.".format(request.POST.get("client_name"))
    elif len(models.Company.objects.filter(short_name=request.POST.get("client_short"))) > 0:
        success = False
        context["content"] += "Short name {} already exist.".format(request.POST.get("client_short"))
    elif len(models.Company.objects.filter(uid=request.POST.get("client_id"))) > 0:
        success = False
        context["content"] += "ID {} already exist.".format(request.POST.get("client_id"))
    elif len(models.Company.objects.filter(code=request.POST.get("client_code"))) > 0:
        success = False
        context["content"] += "Code {} already exist.".format(request.POST.get("client_code"))
    elif len(models.Company.objects.filter(tel=request.POST.get("client_tel"))) > 0:
        success = False
        context["content"] += "Tel {} already exist.".format(request.POST.get("client_tel"))
    elif len(models.Company.objects.filter(website=request.POST.get("client_website"))) > 0:
        success = False
        context["content"] += "Website {} already exist.".format(request.POST.get("client_website"))
    if success:
        client = models.Company(
            name=request.POST.get("client_name"),
            short_name=request.POST.get("client_short"),
            uid=request.POST.get("client_id"),
            code=request.POST.get("client_code"),
            category=request.POST.get("client_category"),
            type=request.POST.get("client_type"),
            level=request.POST.get("client_level"),
            currency=request.POST.get("client_currency"),
            tel=request.POST.get("client_tel"),
            website=request.POST.get("client_website"),
            parent=request.POST.get("client_parent"),
            area=request.POST.get("client_area"),
            employees=request.POST.get("client_employees"),
            revenue=request.POST.get("client_revenue"),
            description=request.POST.get("client_description"),
            owner=request.POST.get("client_owner")
        )
        client.save()
        context["title"] = "Success"
        context["name"] = "Successful Submit"
        data = sorted(request.POST)
        for i in data:
            if i != "csrfmiddlewaretoken":
                context["content"] += "<span class=\"item\">{} : {}</span><br>".format(i, request.POST[i])
        return render(request, 'notice.html', context)
    context["title"] = "Failed"
    context["name"] = "Failed to Submit"
    return render(request, 'notice.html', context)


def edit_client_form(request):
    client = models.Company.objects.get(uid=request.GET["id"])
    context = {}
    context["content"] = ""
    client.name = request.POST.get("client_name")
    client.short_name = request.POST.get("client_short")
    client.uid = request.POST.get("client_id")
    client.code = request.POST.get("client_code")
    client.category = request.POST.get("client_category")
    client.type = request.POST.get("client_type")
    client.level = request.POST.get("client_level")
    client.currency = request.POST.get("client_currency")
    client.tel = request.POST.get("client_tel")
    client.website = request.POST.get("client_website")
    client.parent = request.POST.get("client_parent")
    client.area = request.POST.get("client_area")
    client.employees = request.POST.get("client_employees")
    client.revenue = request.POST.get("client_revenue")
    client.description = request.POST.get("client_description")
    client.owner = request.POST.get("client_owner")
    client.save()
    context["title"] = "Success"
    context["name"] = "Successful Submit"
    data = sorted(request.POST)
    for i in data:
        if i != "csrfmiddlewaretoken":
            context["content"] += "<span class=\"item\">{} : {}</span><br>".format(i, request.POST[i])
    return render(request, 'notice.html', context)


def notice(request):
    context = {}
    context["title"] = "Success"
    context["name"] = "Successful Submit"
    return render(request, 'notice.html', context)


def client(request):
    context = {}
    context["main"] = "Clients"
    context["action"] = "Client List"
    context["page"] = "client"
    context["clients"] = models.Company.objects.all()
    return render(request, 'client.html', context)


def newClient(request):
    context = {}
    context["main"] = "Clients"
    context["action"] = "New Client"
    context["url"] = "/create-client-form/"
    return render(request, 'newClient.html', context)


def editClient(request):
    client = models.Company.objects.get(uid=request.GET["id"])
    context = {}
    context["main"] = "Clients"
    context["action"] = "Edit Client"
    context["url"] = "/edit-client-form/?id={}".format(request.GET["id"])
    context["client_name"] = client.name
    context["client_short"] = client.short_name
    context["client_id"] = client.uid
    context["client_code"] = client.code
    context["client_category"] = client.category
    context["client_type"] = client.type
    context["client_level"] = client.level
    context["client_currency"] = client.currency
    context["client_tel"] = client.tel
    context["client_website"] = client.website
    context["client_parent"] = client.parent
    context["client_area"] = client.area
    context["client_employees"] = client.employees
    context["client_revenue"] = client.revenue
    context["client_description"] = client.description
    context["client_owner"] = client.owner
    # context["client_billing_country"] = client.billing_address
    # context["client_billing_address"] = client.currency
    # context["client_billing_city"] = client.currency
    # context["client_billing_postcode"] = client.currency
    # context["client_billing_state"] = client.currency
    # context["client_postal_country"] = client.currency
    # context["client_postal_address"] = client.currency
    # context["client_postal_city"] = client.currency
    # context["client_postal_postcode"] = client.currency
    # context["client_postal_state"] = client.currency
    return render(request, 'newClient.html', context)

def viewClient(request):
    context = {}
    context["main"] = "Clients"
    context["client"] = models.Company.objects.get(uid=request.GET.get("id"))
    return render(request, 'viewClient.html', context)

def filter(request):
    context = {}
    context["main"] = "Result"
    context["action"] = "Filter result for {}".format(request.GET.get("name"))
    if request.GET.get("name") == "category":
        context["clients"] = models.Company.objects.filter(category=request.GET.get("value")).all()
    elif request.GET.get("name") == "type":
        context["clients"] = models.Company.objects.filter(type=request.GET.get("value")).all()
    elif request.GET.get("name") == "level":
        context["clients"] = models.Company.objects.filter(level=request.GET.get("value")).all()
    elif request.GET.get("name") == "currency":
        context["clients"] = models.Company.objects.filter(currency=request.GET.get("value")).all()
    elif request.GET.get("name") == "parent":
        context["clients"] = models.Company.objects.filter(parent=request.GET.get("value")).all()
    elif request.GET.get("name") == "area":
        context["clients"] = models.Company.objects.filter(area=request.GET.get("value")).all()
    elif request.GET.get("name") == "owner":
        context["clients"] = models.Company.objects.filter(owner=request.GET.get("value")).all()
    else:
        context["clients"] = models.Company.objects.all()
    return render(request, 'client.html', context)
