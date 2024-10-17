import cv2
from ultralytics import YOLO

# Load the YOLOv8 pre-trained model
model = YOLO('yolov8n.pt')  # or yolov8s.pt, yolov8m.pt for different model sizes

def detect_human(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Run the image through YOLOv8
    results = model(image)

    # Check if 'person' class (ID 0) is detected
    human_detected = False
    for result in results[0].boxes:
        class_id = int(result.cls)
        confidence = result.conf
        if class_id == 0:  # Class ID 0 corresponds to 'person'
            human_detected = True
            print(f'Human detected with confidence {confidence.item():.2f}')
            break

    # Return detection result
    return human_detected

if __name__ == "__main__":
    image_path = "images/sample_image7.jpg"  # Path to your test image
    if detect_human(image_path):
        print("Human detected, sending alert...")
        from alert import send_alert
        send_alert()
    else:
        print("No human detected.")
