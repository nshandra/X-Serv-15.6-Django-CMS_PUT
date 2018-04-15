from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from cms.models import Pages
# Create your views here.


def main(request):
    resp = "Available pages: "
    pages = Pages.objects.all()
    for page in pages:
        resp += "<br><a href=/" + page.name + ">" + page.name + "</a>"
    return HttpResponse(resp)


@csrf_exempt
def get_page(request, req_name):
    try:
        req_page = Pages.objects.get(name=req_name).page
        if request.method == "GET":
            return HttpResponse(req_page)
        else:
            return HttpResponseNotFound("<h1>Page already exist.</h1>")
    except Pages.DoesNotExist:
        if request.method == "PUT":
            Pages(name=req_name, page=request.body).save()
            return HttpResponse("Page submitted.<br><br><a href=/>Home</a>")
        else:
            return HttpResponseNotFound("<h1>Page does not exist.</h1>")
