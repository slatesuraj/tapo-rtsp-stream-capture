import cv2

def record_rtsp(rtsp_url, output_file):
  """Records an RTSP stream to a local video file.

  Args:
    rtsp_url: The URL of the RTSP stream.
    output_file: The path to the output video file.
  """

  cap = cv2.VideoCapture(rtsp_url)

  # Check if the video capture is opened successfully
  if not cap.isOpened():
    print("Error opening video capture")
    return

  # Get video properties
  frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
  frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
  fps = cap.get(cv2.CAP_PROP_FPS)

  # Define the codec and create VideoWriter object
  fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can change this to other codecs like 'XVID'
  out = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))

  while True:
    ret, frame = cap.read()

    if not ret:
      break

    out.write(frame)

    # Optionally, display the frame
    # cv2.imshow('frame', frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #   break

  # Release resources
  cap.release()
  out.release()
  # cv2.destroyAllWindows()

if __name__ == "__main__":
  rtsp_url = "your_rtsp_url_here"  # Replace with your RTSP stream URL
  output_file = "output.mp4"
  record_rtsp(rtsp_url, output_file)
