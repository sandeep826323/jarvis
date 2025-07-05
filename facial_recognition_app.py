import cv2
import face_recognition
import numpy as np
import os

# Create arrays of known face encodings and their names
known_face_encodings = []
known_face_names = []

# Flag to track if we're in detection-only mode
detection_only_mode = True

# Path to samples directory
samples_dir = os.path.join("Backend", "samples")

# Try to find a sample image in the samples directory
sample_files = []
if os.path.exists(samples_dir):
    sample_files = [f for f in os.listdir(samples_dir) if f.startswith("face.")]

if sample_files:
    try:
        # Load the first sample image
        sample_path = os.path.join(samples_dir, sample_files[0])
        known_image = face_recognition.load_image_file(sample_path)
        known_face_encoding = face_recognition.face_encodings(known_image)
        if len(known_face_encoding) > 0:
            known_face_encodings.append(known_face_encoding[0])
            # Extract ID from filename (face.ID.number.jpg)
            face_id = sample_files[0].split('.')[1]
            known_face_names.append(f"Person {face_id}")
            detection_only_mode = False
            print(f"Successfully loaded sample from {sample_path}")
        else:
            print(f"Warning: No face found in '{sample_path}'")
    except Exception as e:
        print(f"Error loading sample image: {e}")
else:
    print("Warning: No sample images found in Backend/samples directory.")
    
    # Fall back to checking for known_person.jpg
    if os.path.exists("known_person.jpg"):
        try:
            # Load a sample picture and learn how to recognize it.
            known_image = face_recognition.load_image_file("known_person.jpg")
            known_face_encoding = face_recognition.face_encodings(known_image)
            if len(known_face_encoding) > 0:
                known_face_encodings.append(known_face_encoding[0])
                known_face_names.append("Person 1")
                detection_only_mode = False
            else:
                print("Warning: No face found in 'known_person.jpg'")
        except Exception as e:
            print(f"Error loading 'known_person.jpg': {e}")
    else:
        print("Warning: 'known_person.jpg' not found.")
    
    if os.path.exists("known_person2.jpg"):
        try:
            # Load another sample picture and learn how to recognize it.
            known_image2 = face_recognition.load_image_file("known_person2.jpg")
            known_face_encoding2 = face_recognition.face_encodings(known_image2)
            if len(known_face_encoding2) > 0:
                known_face_encodings.append(known_face_encoding2[0])
                known_face_names.append("Person 2")
                detection_only_mode = False
            else:
                print("Warning: No face found in 'known_person2.jpg'")
        except Exception as e:
            print(f"Error loading 'known_person2.jpg': {e}")
    else:
        print("Warning: 'known_person2.jpg' not found.")

# If no known faces were loaded, print a message and switch to detection-only mode
if detection_only_mode:
    print("No known faces were loaded. Running in DETECTION-ONLY mode.")
    print("To enable face recognition, add image files named 'known_person.jpg' and/or 'known_person2.jpg'")
    print("to the same directory as this script, or modify the script to use your own images.")

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

# Try multiple ways to open the camera
camera_opened = False
video_capture = None

# Try with default camera (0)
print("Attempting to access camera...")
try:
    video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if video_capture.isOpened():
        camera_opened = True
        print("Successfully opened camera with CAP_DSHOW")
except Exception as e:
    print(f"Error with CAP_DSHOW: {e}")

# If that failed, try without CAP_DSHOW
if not camera_opened:
    try:
        video_capture = cv2.VideoCapture(0)
        if video_capture.isOpened():
            camera_opened = True
            print("Successfully opened camera without CAP_DSHOW")
    except Exception as e:
        print(f"Error opening default camera: {e}")

# If still failed, try camera 1
if not camera_opened:
    try:
        video_capture = cv2.VideoCapture(1)
        if video_capture.isOpened():
            camera_opened = True
            print("Successfully opened camera 1")
    except Exception as e:
        print(f"Error opening camera 1: {e}")

if not camera_opened:
    print("Error: Could not open any video capture device (webcam).")
    print("Please ensure your webcam is properly connected and not in use by another application.")
    exit()

print("Face detection is now running. Press 'q' to quit.")

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()
    
    if not ret:
        print("Error: Failed to grab frame from webcam. Retrying...")
        # Try to release and reopen the camera
        video_capture.release()
        video_capture = cv2.VideoCapture(0)
        if not video_capture.isOpened():
            print("Could not reconnect to webcam. Exiting.")
            break
        continue

    # Only process every other frame of video to save time
    if process_this_frame:
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]
        
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        
        face_names = []
        
        if not detection_only_mode and len(face_locations) > 0:
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"
                
                # Use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                
                face_names.append(name)
        else:
            # In detection-only mode, just label all faces as "Unknown"
            face_names = ["Detected Face"] * len(face_locations)
    
    process_this_frame = not process_this_frame
    
    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        
        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        
        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
    
    # Add information about mode
    mode_text = "DETECTION ONLY MODE" if detection_only_mode else "RECOGNITION MODE"
    cv2.putText(frame, mode_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    
    # Display the resulting image
    cv2.imshow('Face Recognition', frame)
    
    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows() 