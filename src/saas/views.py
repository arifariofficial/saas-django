from django.shortcuts import render


def home_page(request, *args, **kwargs):
    my_title = "Home Page"
    context = {
        "page_title": my_title,
    }
    return render(request, "home.html", context)
