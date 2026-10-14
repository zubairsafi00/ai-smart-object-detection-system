from ultralytics import YOLO
import cv2

# Load YOLO model
from pathlib import Path
from ultralytics import YOLO

BASE_DIR = Path(__file__).resolve().parent
model = YOLO(BASE_DIR / "yolov8n.pt")

# Open camera
cap = cv2.VideoCapture(0)

window_name = "AI Smart Radar"

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    annotated_frame = frame.copy()
    object_count = 0

    for box in results[0].boxes:
        object_count += 1

        # Get class and confidence
        cls_id = int(box.cls[0])
        confidence = float(box.conf[0]) * 100
        label = model.names[cls_id]

        # Get bounding box coordinates
        x1, y1, x2, y2 = map(int, box.xyxy[0])

        # Calculate box area (for distance estimation)
        box_width = x2 - x1
        box_height = y2 - y1
        box_area = box_width * box_height

        # Simple distance estimation
        if box_area > 150000:
            distance = "Very Close"
        elif box_area > 70000:
            distance = "Close"
        elif box_area > 30000:
            distance = "Medium"
        else:
            distance = "Far"

        # Create label text
        text = f"{label} {confidence:.1f}% - {distance}"

        # Draw rectangle
        cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Draw text
        cv2.putText(
            annotated_frame,
            text,
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

    # Show object counter
    cv2.putText(
        annotated_frame,
        f"Objects Detected: {object_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        3
    )

    cv2.imshow(window_name, annotated_frame)

    key = cv2.waitKey(1)

    # Press Q to exit
    if key == ord("q"):
        break

    # Close if window ❌ pressed
    if cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv2.destroyAllWindows()