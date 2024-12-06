from django.shortcuts import render

MENU = {"Main page": "/", "About Us": "/about", "Posts": "/post", "Reviews": "/reviews"}

def main_page(request):
    title = "Main page"
    data = {"menu": MENU, "title": title}
    return render(request, "./index.html", context=data)

def about_page(request):
    title = "About Us"
    data = {"menu": MENU, "title": title}
    return render(request, "./about.html", context=data)

def post_page(request, id=1):
    resp = f'Post {id}'
    title = "Posts"
    data = {"menu": MENU, "title": title, "id": id, "resp": resp}
    return render(request, "./post.html", context=data)

