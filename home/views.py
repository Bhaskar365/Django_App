from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "ViewVar" : "This is a sample text from views.py"
    }
    return render(request, 'index.html')
    # return HttpResponse("This is home page")

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')