from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def details(request, pk):
    return render(request, 'dashboard/details.html')
