import os
import uuid

from django.conf import settings
from ultralytics import YOLO
import cv2

#Use nano version of yolo
model = YOLO("yolov8n.pt")

def detect_people_yolo(image_path, output_subfolder='yolo'):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Image not found: {image_path}")
        return None, 0

    results = model(image)
    people = [box for box in results[0].boxes.data if int(box[-1]) == 0]
    num_people_detected = len(people)

    for box in people:
        x1, y1, x2, y2, score, cls = box
        cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)

    # Create output folder if needed
    output_path = os.path.join(settings.MEDIA_ROOT, 'uploads', output_subfolder)
    os.makedirs(output_path, exist_ok=True)

    filename = f"{uuid.uuid4()}.jpg"
    result_full_path = os.path.join(output_path, filename)
    saved = cv2.imwrite(result_full_path, image)

    if saved:
        return f'uploads/{output_subfolder}/{filename}', num_people_detected
    else:
        return None, num_people_detected
