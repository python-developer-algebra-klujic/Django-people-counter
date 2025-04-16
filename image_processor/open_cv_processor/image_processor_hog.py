import os
import uuid

import cv2
from django.conf import settings


def detect_people_hog(image_path, output_subfolder='hog'):
    image = cv2.imread(image_path)

    if image is None:
        print(f"Image not found: {image_path}")
        return None, 0

    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    (regions, _) = hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale=1.05)
    num_people_detected = len(regions)

    for (x, y, w, h) in regions:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Output directory in media/uploads/hog/
    output_dir = os.path.join(settings.MEDIA_ROOT, 'uploads', output_subfolder)
    os.makedirs(output_dir, exist_ok=True)

    # Save image as UUID .jpg
    filename = f"{uuid.uuid4()}.jpg"
    result_full_path = os.path.join(output_dir, filename)
    saved = cv2.imwrite(result_full_path, image)

    if saved:
        # return relative MEDIA path
        return f'uploads/{output_subfolder}/{filename}', num_people_detected
    else:
        print("Couldn't save image.")
        return None, num_people_detected