# tapo-rtsp-stream-capture

The TP-Link Tapo camera device provides an rtsp feed for its video. Once a username and password is set in the app, it is available on: rtsp://user:pass@192.168.a.b:554/stream1
Use this link to setup username:password https://www.tapo.com/in/faq/34/

## Dependencies
Run below command to install project dependencies.
```sudo pip3 install -r requirements.txt```

## Setup
Update rtsp url in record_rtsp.py file and run below command
```python record_rtsp.py```

By running this script, the RTSP stream will be recorded as an MP4 file named output.mp4 in the same directory. You can adjust the output file format and name as needed.

## Code explaination
1. Import OpenCV: Imports the necessary library.
2. Define record_rtsp function:
   a. Takes RTSP URL and output file path as input.
   b. Creates a VideoCapture object to capture the RTSP stream.
   c. Gets video properties (width, height, FPS).
   d. Defines the video codec and creates a VideoWriter object.
   e. Reads frames from the capture, writes them to the output file.
   f. Optionally, displays the frame (commented out).
   e. Releases resources.
3. Main block:
   a. Sets RTSP URL and output file path.
   b. Calls record_rtsp function to start recording.
