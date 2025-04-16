from django.shortcuts import redirect, render

from .open_cv_processor.image_processor_hog import detect_people_hog
from .open_cv_processor.image_processor_yolo import detect_people_yolo
from .models import PeopleCounter

# Create your views here.
def upload_image(request):
    if request.method == "POST" and request.FILES.get('image'):
        uploaded_file = request.FILES['image']

        people_counter = PeopleCounter()
        people_counter.original_file.save(uploaded_file.name, uploaded_file)
        people_counter.save()

        yolo_file, yolo_counter = detect_people_yolo(people_counter.original_file.path)
        if yolo_file:
            people_counter.yolo_counter = yolo_counter
            people_counter.yolo_processed_file.name = yolo_file

        hog_file, hog_counter = detect_people_hog(people_counter.original_file.path)
        if hog_file:
            people_counter.hog_counter = hog_counter
            people_counter.hog_processed_file.name = hog_file


        people_counter.save()

        return redirect('dashboard:dashboard')
    return render(request, 'image_processor/image-upload.html')
