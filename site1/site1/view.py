from django.http import HttpResponse

def main_page(request):
    return HttpResponse("main page")

def about(request):
    return HttpResponse("about")

def post(request):
    return HttpResponse("post")