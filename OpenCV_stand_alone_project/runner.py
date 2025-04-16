import argparse
from image_processor_yolo import detect_people_yolo
from image_processor_hog import detect_people_hog

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process image.")
    parser.add_argument("--input1", required=True, help="Path to the first image")
    parser.add_argument("--input2", required=True, help="Path to the second1 image")
    parser.add_argument("--output", required=True, help="Path to the output folder")

    args = parser.parse_args()
    image_path_1 = args.input1
    image_path_2 = args.input2
    output_path = args.output

    number_of_people = detect_people_yolo(image_path_1, output_path)
    print(f"Number of detected people on image: {number_of_people}")
    number_of_people = detect_people_yolo(image_path_2, output_path)
    print(f"Number of detected people on image: {number_of_people}")

    number_of_people = detect_people_hog(image_path_1, output_path)
    print(f"Number of detected people on image: {number_of_people}")
    number_of_people = detect_people_hog(image_path_2, output_path)
    print(f"Number of detected people on image: {number_of_people}")