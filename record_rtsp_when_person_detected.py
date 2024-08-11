import cv2
import mediapipe as mp
import time

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Initialize MediaPipe Drawing utilities
mp_draw = mp.solutions.drawing_utils

# RTSP stream URL
rtsp_url = "your_rtsp_stream_url_here"

# Video writer
out = None

# Function to check if a person is detected
def is_person_detected(results):
    return bool(results.pose_landmarks)

def main():
    out = None
    cap = cv2.VideoCapture(rtsp_url)

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            break

        # Convert the BGR image to RGB.
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


        # Process the image with MediaPipe Pose
        results = pose.process(image)

        # Convert back to BGR for OpenCV visualization
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Draw pose landmarks
        if results.pose_landmarks:
            mp_draw.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Check if person is detected
        if is_person_detected(results):
            if out is None:
                # Start recording
                fourcc = cv2.VideoWriter_fourcc(*'XVID')
                out = cv2.VideoWriter('output.avi', fourcc, 20.0, (image.shape[1], image.shape[0]))
                start_time = time.time()
            out.write(image)
        else:
            # Stop recording if no person for a certain duration
            if out is not None:
                if time.time() - start_time > 5:  # Adjust the duration as needed
                    out.release()
                    out = None

        cv2.imshow("MediaPipe Pose", image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    if out is not None:
        out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
