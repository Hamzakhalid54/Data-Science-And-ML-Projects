import cv2
import numpy as np
from ultralyticsplus import YOLO, render_result

# Load pothole detection model
pothole_model = YOLO('keremberke/yolov8s-pothole-segmentation')

# Load vehicle detection model
vehicle_model = YOLO('ultralytics/yolov8n')

# Set video path
video_path = r'C:\Users\Hamza Khalid\Desktop\Trimmed.mp4'

# Define window size
window_width = 800
window_height = 600

# Open the video file
cap = cv2.VideoCapture(video_path)

while(cap.isOpened()):
    # Read frame from video
    ret, frame = cap.read()
    if ret:
        # Perform vehicle detection
        vehicle_results = vehicle_model.predict(frame)

        # Render vehicle detection results on the frame
        render_vehicle = render_result(model=vehicle_model, image=frame, result=vehicle_results[0])

        # Perform pothole detection
        pothole_results = pothole_model.predict(frame)

        # Render pothole detection results on the frame
        render_pothole = render_result(model=pothole_model, image=frame, result=pothole_results[0])

        # Combine both renderings
        render_vehicle = np.array(render_vehicle)
        render_pothole = np.array(render_pothole)
        render_combined = cv2.addWeighted(render_vehicle, 0.5, render_pothole, 0.5, 0)

        # Resize the frame
        render_combined = cv2.resize(render_combined, (window_width, window_height))

        # Display the frame using cv2.imshow()
        cv2.imshow('Frame', render_combined)

        # Quit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release the video capture and close windows
cap.release()
cv2.destroyAllWindows()
