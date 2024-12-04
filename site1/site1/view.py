from django.http import HttpResponse
from django.shortcuts import render

MENU = {"Main page": "/", "About Us": "/about", "Posts": "/post"}

def main_page(request):
    title = "Main page"
    data = {"menu": MENU, "title": title}
    return render(request, "./index.html", context=data)

def about_page(request):
    title = "About Us"
    data = {"menu": MENU, "title": title}
    return render(request, "./about.html", context=data)

def post_page(request):
    title = "Posts"
    data = {"menu": MENU, "title": title}
    return render(request, "./post.html", context=data)