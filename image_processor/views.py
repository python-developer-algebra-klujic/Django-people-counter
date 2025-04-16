from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def upload_image(request):
    return HttpResponse('Image upload is working!')
