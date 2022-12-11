from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("This is Home Page")
    return render(request, 'index.html')

def about(request):
    # return HttpResponse("This is About Page")
    return render(request, 'about.html')

# def services(request):
#     return HttpResponse("This is Services Page")

def classes(request):
    return render(request, 'classes.html')

def signup(request):
    return render(request, 'signuppage.html')

def contact(request):
    # return HttpResponse("This is Contact Page")
    return render(request, "index.html#contact")