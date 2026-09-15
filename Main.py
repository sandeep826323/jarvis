import sys
import os
from datetime import datetime, timedelta
import psutil  # You'll need to install this package: pip install psutil
import string
from Backend.auto_updater import AutoUpdater
from Backend.e2e_encryption import E2EEncryption
from Backend.simple_pattern_recognition import SimplePatternRecognition as PatternRecognition
from Backend.simple_personalization_engine import SimplePersonalizationEngine
from Backend.simple_predictive_assistance import SimplePredictiveAssistance
from Backend.simple_privacy_mode import SimplePrivacyMode as PrivacyMode
from Backend.reminder import ReminderSystem
from Backend.simple_reinforcement_learning import SimpleReinforcementLearning, LearningStrategy  # Import both
from Backend.system_monitor import SystemMonitor
from Backend.whatsapp import WhatsAppGroqAssistant, get_contact_number
import webbrowser
import json
import logging
import traceback
from collections import defaultdict
from typing import Optional, List, Dict, Any

# Initialize auto updater and e2e encryption
auto_updater = AutoUpdater(app_name="jarvis")
e2e_encryption = E2EEncryption(identity="jarvis")

# Global instances for personalization and predictive assistance
personalization_engine = None
pattern_recognition = None
predictive_assistance = None
privacy_mode = None
reminder_system = None
reinforcement_learning = None
system_monitor = None

# Ensure data directories exist
os.makedirs("Backend/Data", exist_ok=True)
os.makedirs("Backend/config", exist_ok=True)
os.makedirs("logs", exist_ok=True)

# Initialize personalization engine with proper path
try:
    # Create data directory if it doesn't exist
    os.makedirs("Backend/Data", exist_ok=True)
    
    personalization_data_path = "Backend/Data/personalization_data.json"
    if not os.path.exists(personalization_data_path):
        default_data = {
            "interactions": [],
            "preferences": {
                "general": {
                    "theme": "light",
                    "language": "en",
                    "notifications_enabled": True
                },
                "voice": {
                    "voice_enabled": True,
                    "voice_speed": 1.0,
                    "voice_volume": 1.0
                },
                "privacy": {
                    "level": "medium",
                    "data_collection": True
                }
            },
            "last_updated": datetime.now().isoformat()
        }
        with open(personalization_data_path, 'w') as f:
            json.dump(default_data, f, indent=2)
    
    personalization_engine = SimplePersonalizationEngine(data_path=personalization_data_path)
    print("✓ Personalization engine initialized successfully")
except Exception as e:
    print(f"✗ Error initializing personalization engine: {e}")
    personalization_engine = None

# Initialize reinforcement learning with proper strategy
try:
    # Create rl_data.json if it doesn't exist
    rl_data_path = "Backend/Data/rl_data.json"
    if not os.path.exists(rl_data_path):
        default_rl_data = {
            "actions_history": [],
            "rewards_history": [],
            "q_values": {},
            "action_counts": {},
            "total_rewards": {},
            "last_updated": datetime.now().isoformat()
        }
        with open(rl_data_path, 'w') as f:
            json.dump(default_rl_data, f, indent=2)
    
    reinforcement_learning = SimpleReinforcementLearning(
        user_id="mahto sandeep",
        data_path=rl_data_path,
        strategy=LearningStrategy.EPSILON_GREEDY.value,  # Use enum value
        learning_rate=0.1,
        exploration_rate=0.2
    )
    print("✓ Reinforcement learning initialized successfully")
except Exception as e:
    print(f"✗ Error initializing reinforcement learning: {e}")
    reinforcement_learning = None

# Initialize system monitor with proper config
try:
    # Create config directory if it doesn't exist
    os.makedirs("Backend/config", exist_ok=True)
    
    # Create monitor config if it doesn't exist
    monitor_config_path = "Backend/config/monitor_config.json"
    if not os.path.exists(monitor_config_path):
        default_config = {
            "thresholds": {
                "cpu_percent": 85,
                "memory_percent": 85,
                "disk_percent": 90,
                "battery_percent": 15
            },
            "monitoring_interval": 60,
            "enable_alerts": True,
            "log_level": "INFO",
            "save_history": True,
            "history_retention_days": 7
        }
        with open(monitor_config_path, 'w') as f:
            json.dump(default_config, f, indent=2)
    
    system_monitor = SystemMonitor(
        log_dir="logs",
        config_path=monitor_config_path
    )
    print("✓ System monitor initialized successfully")
except Exception as e:
    print(f"✗ Error initializing system monitor: {e}")
    system_monitor = None

# Run cleanup for speech files
try:
    from cleanup_scripts.cleanup_speech import cleanup_speech_files
    cleanup_speech_files()  # Clean up any existing speech files to prevent conflicts
except Exception as e:
    print(f"Warning: Could not run speech file cleanup: {e}")

# Fix paths for both development and PyInstaller
if getattr(sys, 'frozen', False):
    # Running as compiled executable
    base_path = os.path.dirname(sys.executable)
    # Add the dist folder and its subdirectories to pathC:\Users\alpha\OneDrive\Desktop\jarvis\Frontend
    sys.path.append(base_path)
    sys.path.append(os.path.join(base_path, r'F:\jarvis\Frontend'))
    sys.path.append(os.path.join(base_path, r'F:\jarvis\Frontend'))
else:
    # Running as script
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(base_path) #F:\jarvis\Frontend
    sys.path.append(os.path.join(base_path, r'F:\jarvis\Frontend'))
    sys.path.append(os.path.join(base_path, r'F:\jarvis\Frontend'))

print(f"Final Python path: {sys.path}")  # Debugging

# Now try importing
try:
    from Frontend.GUI import (
        graphical_user_interface,
        set_assistant_status,
        show_text_to_screen,
        temp_directory_path,
        set_microphone_status,
        answer_modifier,
        query_modifier,
        get_microphone_status
    )
    print("Successfully imported Frontend.GUI")  # Debugging
except ImportError as e:
    print(f"Import failed: {e}")  # Debugging
    raise
from Backend.Model import FirstLayerDMM
from Backend.query_manager import QueryManager
from Backend.RealtimeSearchEngine import RealtimeSearchEngine
from Backend.Automation import Automation
from Backend.SpeechToText import SpeechRecognition
from Backend.Chatbot import Chatbot

from Backend.TextToSpeech import TextToSpeech
from dotenv import dotenv_values
from asyncio import run
from time import sleep
import subprocess
import logging
import threading
import json
import os
import cv2
import numpy as np
from PIL import Image #pillow package
import pyautogui as p
from tkinter import filedialog, Tk
from PIL import Image
import time  # Import time for periodic checks
from plyer import notification 
# Import hand_main conditionally to prevent startup crashes
# from Backend.hand_main import (
#    Config, cap, detector, mode, active, get_finger_state,
#    handle_cursor_mode, handle_scroll_mode, handle_volume_mode, handle_zoom_mode
# )
from Backend.call import make_call, find_contact_in_log, import_contacts_from_csv, add_contact, open_whatsapp_app  # Import available functions




env_vars = dotenv_values(".env")
Username = ("mahto sandeep")
Assistantname = ("jarvis")
DefaultMessage = f'''{Username} : Hello {Assistantname}, How are you?
{Assistantname} : Welcome {Username}. I am doing well. How may i help you?'''
subprocesses = []
Functions = ["open", "close", "play", "system", "content", "google search", "youtube search", "video call", "make video call", "audio call", "make audio call"]

# Configure logging
logging.basicConfig(filename='assistant.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to speak the initialization text
def speak_text():
    initialization_message = "Initializing all systems, now I am online"
    TextToSpeech(initialization_message)
    
# Function to start emotion detection
def start_emotion_detection():
    try:
        print("=== Starting emotion detection function ===")
        
        # Check if OpenCV is available
        try:
            import cv2
            print("OpenCV imported successfully")
        except ImportError:
            message = "OpenCV is not installed. Please install it with: pip install opencv-python"
            print(message)
            TextToSpeech(message)
            show_text_to_screen(f"{Assistantname} : {message}")
            return message
        
        # Initialize webcam
        print("Initializing webcam...")
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        
        if not cap.isOpened():
            message = "Could not access the camera. Please make sure it's connected and not being used by another application."
            print(message)
            TextToSpeech(message)
            show_text_to_screen(f"{Assistantname} : {message}")
            return message
        
        # Load face detection cascade
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        
        # Simple emotion list (we won't actually detect emotions, just simulate it)
        emotions = ['Happy', 'Sad', 'Neutral', 'Surprised', 'Angry']
        
        show_text_to_screen(f"{Assistantname} : Emotion detection is running. Press 'q' to quit.")
        
        import random
        frame_count = 0
        current_emotion = "Neutral"
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            # Convert to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # Detect faces
            faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30)
            )
            
            # Every 30 frames, randomly change the emotion for demo purposes
            frame_count += 1
            if frame_count % 30 == 0:
                current_emotion = random.choice(emotions)
                confidence = random.uniform(0.7, 0.95)
                print(f"Detected emotion: {current_emotion} ({confidence:.2f})")
            
            # Draw rectangle around faces and show emotion
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                # Add text for the emotion
                cv2.putText(frame, 
                           f"{current_emotion}", 
                           (x, y-10), 
                           cv2.FONT_HERSHEY_SIMPLEX, 
                           0.9, 
                           (0, 255, 0), 
                           2)
            
            # Display FPS
            cv2.putText(frame, 
                      f"Demo Mode - No real detection", 
                      (10, 30), 
                      cv2.FONT_HERSHEY_SIMPLEX, 
                      0.7, 
                      (0, 0, 255), 
                      2)
            
            # Display the frame
            cv2.imshow("Emotion Detection (Demo)", frame)
            
            # Break loop with 'q' key
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
        cap.release()
        cv2.destroyAllWindows()
        return "Emotion detection stopped"
    except Exception as e:
        error_msg = f"Error in emotion detection: {str(e)}"
        print(error_msg)
        TextToSpeech(error_msg)
        show_text_to_screen(f"{Assistantname} : {error_msg}")
        return error_msg

# Function to start object detection
def start_object_detection():
    try:
        print("=== Starting object detection function ===")
        
        # Import the ObjectDetection class
        try:
            from Backend.object_detection import ObjectDetection
            print("Object Detection module imported successfully")
        except ImportError as e:
            message = f"Object Detection module could not be imported: {str(e)}"
            print(message)
            TextToSpeech(message)
            show_text_to_screen(f"{Assistantname} : {message}")
            return message
        
        # Initialize webcam
        print("Initializing webcam...")
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        
        if not cap.isOpened():
            message = "Could not access the camera. Please make sure it's connected and not being used by another application."
            print(message)
            TextToSpeech(message)
            show_text_to_screen(f"{Assistantname} : {message}")
            return message
        
        # Initialize object detection with MobileNet (fastest model)
        detector = ObjectDetection(model_type="mobilenet", confidence_threshold=0.5)
        
        show_text_to_screen(f"{Assistantname} : Object detection is running. Press 'q' to quit.")
        TextToSpeech("Starting object detection with MobileNet. I'll identify objects in view.")
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            # Detect objects in the frame
            try:
                detections = detector.detect_objects(frame)
                
                # Visualize detections on the frame
                result_frame = detector.visualize_detections(frame.copy(), detections)
                
                # Get performance metrics
                metrics = detector.get_performance_metrics()
                fps = metrics.get("fps", 0)
                
                # Display FPS
                cv2.putText(result_frame, 
                          f"FPS: {fps:.1f}", 
                          (10, 30), 
                          cv2.FONT_HERSHEY_SIMPLEX, 
                          0.7, 
                          (0, 0, 255), 
                          2)
                
                # Display summary of detected objects
                if len(detections) > 0:
                    objects_text = ", ".join([d['class'] for d in detections[:3]])
                    if len(detections) > 3:
                        objects_text += f" and {len(detections)-3} more"
                    cv2.putText(result_frame, 
                              f"Detected: {objects_text}", 
                              (10, 60), 
                              cv2.FONT_HERSHEY_SIMPLEX, 
                              0.6, 
                              (0, 255, 0), 
                              2)
                
                # Display the frame
                cv2.imshow("Object Detection", result_frame)
                
            except Exception as e:
                print(f"Error during detection: {e}")
                # If detection fails, just show the original frame
                cv2.putText(frame, 
                          f"Detection error: {str(e)[:50]}", 
                          (10, 30), 
                          cv2.FONT_HERSHEY_SIMPLEX, 
                          0.7, 
                          (0, 0, 255), 
                          2)
                cv2.imshow("Object Detection", frame)
            
            # Break loop with 'q' key
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
        cap.release()
        cv2.destroyAllWindows()
        return "Object detection stopped"
    except Exception as e:
        error_msg = f"Error in object detection: {str(e)}"
        print(error_msg)
        TextToSpeech(error_msg)
        show_text_to_screen(f"{Assistantname} : {error_msg}")
        return error_msg

# Function to start simple object detection (without TensorFlow)
# def start_simple_object_detection():
    try:
        print("=== Starting simple object detection ===")
        
        # Import the SimpleObjectDetection class
        try:
            from Backend.simple_object_detection import SimpleObjectDetection
            print("Simple Object Detection module imported successfully")
        except ImportError as e:
            message = f"Simple Object Detection module could not be imported: {str(e)}"
            print(message)
            TextToSpeech(message)
            show_text_to_screen(f"{Assistantname} : {message}")
            return message
        
        # Initialize webcam
        print("Initializing webcam...")
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        
        if not cap.isOpened():
            message = "Could not access the camera. Please make sure it's connected and not being used by another application."
            print(message)
            TextToSpeech(message)
            show_text_to_screen(f"{Assistantname} : {message}")
            return message
        
        # Initialize simple object detection
        detector = SimpleObjectDetection(confidence_threshold=0.5)
        
        show_text_to_screen(f"{Assistantname} : Simple object detection is running. Press 'q' to quit.")
        TextToSpeech("Starting simple object detection. I'll identify objects in view.")
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            # Detect objects in the frame
            try:
                detections = detector.detect_objects(frame)
                
                # Visualize detections on the frame
                result_frame = detector.visualize_detections(frame.copy(), detections)
                
                # Get summary of what was detected
                if detections:
                    summary = detector.summarize_detection(detections)
                    print(summary)
                
                # Display the frame
                cv2.imshow("Simple Object Detection", result_frame)
                
            except Exception as e:
                print(f"Error during detection: {e}")
                # If detection fails, just show the original frame
                cv2.putText(frame, 
                          f"Detection error: {str(e)[:50]}", 
                          (10, 30), 
                          cv2.FONT_HERSHEY_SIMPLEX, 
                          0.7, 
                          (0, 0, 255), 
                          2)
                cv2.imshow("Simple Object Detection", frame)
            
            # Break loop with 'q' key
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
        cap.release()
        cv2.destroyAllWindows()
        return "Simple object detection stopped"
    except Exception as e:
        error_msg = f"Error in simple object detection: {str(e)}"
        print(error_msg)
        TextToSpeech(error_msg)
        show_text_to_screen(f"{Assistantname} : {error_msg}")
        return error_msg

recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms

trainer_path = r'F:\jarvis\Backend\trainer\trainer.yml'
if not os.path.exists(trainer_path):
    print(f"Error: File {trainer_path} does not exist.")
else:
    recognizer.read(trainer_path)

cascadePath = r'F:\jarvis\haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascadePath) #initializing haar cascade for object detection approach

font = cv2.FONT_HERSHEY_SIMPLEX #denotes the font type

def taskrun():
    p.press('esc')
    TextToSpeech("verification successful")
    TextToSpeech("welcome back mahto sandeep sir")

#id
id = 0
# names related to ids: example ==> Marcelo: id=1,  etc
names = ['None', 'mahto Sandeep', 'Jay', 'Ilza', 'Z', 'W', ''] # Corrected typo and added placeholder

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) #cv2.CAP_DSHOW to remove warning   

if not cam.isOpened():
    print("Error: Could not open video device")
    # Handle the error (exit or continue without facial recognition)
cam.set(3, 640) # set video FrameWidht
cam.set(4, 480) # set video FrameHeight

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

# flag = True

while True:

    ret, img =cam.read() #read the frames using the above created object

    converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #The function converts an input image from one color space to another

    faces = faceCascade.detectMultiScale( 
        converted_image,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )

    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) #used to draw a rectangle on any image

        id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w]) #to predict on every single image

        # Check if accuracy is less them 100 ==> "0" is perfect match 
        if (accuracy < 100):
            id = names[id]
            accuracy = "{0}%".format(round(100 - accuracy)) # Corrected format string index
            taskrun()

        else:
            id = "unknown"
            accuracy = "  {0}%".format(round(100 - accuracy))
        
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
    cv2.imshow('camera',img) 

    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    
print("Thanks for using this program, have a good day.")
cam.release()
cv2.destroyAllWindows()

# Path to the directory containing training images
training_data_path = r'Backend/samples'

# Initialize the recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Initialize variables for training
training_images = []
labels = []

# Load training images and labels
if os.path.exists(training_data_path):
    for label_id, person_name in enumerate(os.listdir(training_data_path)):
        person_path = os.path.join(training_data_path, person_name)
        if os.path.isdir(person_path):
            for image_file in os.listdir(person_path):
                image_path = os.path.join(person_path, image_file)
                image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
                if image is not None:
                    training_images.append(image)
                    labels.append(label_id)

# Train the recognizer
if training_images and labels:
    recognizer.train(training_images, np.array(labels))
    recognizer.save(r'Backend\trainer\trainer.yml')
    print("Training completed and model saved to 'Backend/trainer/trainer.yml'")
else:
    print("No training data found. Please add images to the training_data directory.")

def ShowDefaultChatIfNoChats():
    try:
        with open(r'F:\jarvis\Data\ChatLog.json', "r", encoding='utf-8') as File:
            content = File.read()
            if len(content) < 5:
                with open(temp_directory_path(r'F:\jarvis\Frontend\Graphics\Database.data'), 'w', encoding='utf-8') as file:
                    file.write("")

                with open(temp_directory_path(r'F:\jarvis\Frontend\Graphics\Responses.data'), 'w', encoding='utf-8') as file:
                    file.write(DefaultMessage)
    except FileNotFoundError:
        # If ChatLog.json doesn't exist, create default files
        with open(temp_directory_path(r'F:\jarvis\Frontend\Graphics\Database.data'), 'w', encoding='utf-8') as file:
            file.write("")

        with open(temp_directory_path(r'F:\jarvis\Frontend\Graphics\Responses.data'), 'w', encoding='utf-8') as file:
            file.write(DefaultMessage)

ShowDefaultChatIfNoChats()
from datetime import datetime

def wish_me():
    """Greet the user with sophistication and warmth, like Jarvis from Iron Man"""
    hour = datetime.now().hour
    if 0 <= hour < 12:
        greeting = "Good Morning"
    elif 12 <= hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"
    
    greeting_message = (
        f"{greeting} {Username} sir. *with warm enthusiasm* "
        "I am delighted to see you again. "
        f"Allow me to reintroduce myself - I am {Assistantname}, "
        "your personal artificial intelligence assistant. "
        "*with pride* I am equipped with state-of-the-art capabilities "
        "to assist you with any task, 24 hours a day, 7 days a week. "
        "*professionally* I am now importing all preferences for your home interface. "
        "*with confidence* All systems are fully operational and at your disposal, sir."
    )
    TextToSpeech(greeting_message)
    show_text_to_screen(f"{Assistantname}: {greeting_message}")



def convert_image_to_pdf():
    try:
        print("convert_image_to_pdf function called.")  # Debugging
        # Initialize Tkinter (hidden window)
        root = Tk()
        root.withdraw()
        
        # Ask user to select multiple image files
        image_paths = filedialog.askopenfilenames(
            title="Select Image Files",
            filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.gif")]
        )
        
        if not image_paths:
            print("No images selected.")
            return "No images selected"
            
        print(f"Selected images: {image_paths}")  # Debugging
        
        # Create PDF path in Downloads folder with a unique name
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        if not os.path.exists(downloads_path):
            os.makedirs(downloads_path)
        
        # Generate a unique filename using a timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        pdf_filename = f"combined_images_{timestamp}.pdf"
        pdf_path = os.path.join(downloads_path, pdf_filename)
        
        # Convert images to PDF
        images = []
        for image_path in image_paths:
            try:
                img = Image.open(image_path)
                if img.mode == 'RGBA':
                    img = img.convert('RGB')
                images.append(img)
            except Exception as e:
                print(f"Error processing image {image_path}: {e}")
            
        
        if not images:
            print("No valid images to convert.")
            return "No valid images to convert"
        
        # Save first image as PDF and append others
        images[0].save(pdf_path, "PDF", resolution=100.0, save_all=True, append_images=images[1:])
        
        # Notify the user
        message = f"{Username} sir, Image to PDF conversion successful. PDF saved at download folder. Can I open it? Yes or No."
        print(message)
        TextToSpeech(message)
        
        # Get user input
        user_response = input("Enter your response (yes or no): ").strip().lower()
        if user_response == "yes":
            os.startfile(pdf_path)  # Open the PDF
            return f"PDF opened successfully at"
        else:
            return f"PDF saved successfully at download folder, but not opened."
        
    except Exception as e:
        print(f"Error converting images to PDF: {e}")
        return f"Error converting images to PDF: {str(e)}"



def ReadChatLogJson():
    with open(r'F:\jarvis\Data\ChatLog.json', 'r', encoding='utf-8') as file:
        chatlog_data = json.load(file)
    return chatlog_data

def ChatLogIntegration():
    json_data = ReadChatLogJson()
    formatted_chatlog = ""
    for entry in json_data:
        if entry["role"] == "user":
            formatted_chatlog += f"User: {entry['content']}\n"
        elif entry["role"] == "assistant":
            formatted_chatlog += f"Assistant: {entry['content']}\n"
    formatted_chatlog = formatted_chatlog.replace("User", Username + " ")
    formatted_chatlog = formatted_chatlog.replace("Assistant", Assistantname + " ")

    # Handle the case when answer_modifier returns None
    modified_chatlog = answer_modifier(formatted_chatlog)
    if modified_chatlog is None:
        modified_chatlog = formatted_chatlog  # Fall back to the original if modified is None

    with open(temp_directory_path(r'F:\jarvis\Frontend\Graphics\Database.data'), 'w', encoding='utf-8') as file:
        file.write(modified_chatlog)

def ShowChatsOnGUI():
    File = open(temp_directory_path(r'F:\jarvis\Frontend\Graphics\Database.data'), "r", encoding='utf-8')
    Data = File.read()
    if len(str(Data))>0:
        lines = Data.split('\n')
        result = '\n'.join(lines)
        File.close()
        File = open(temp_directory_path(r'F:\jarvis\Frontend\Graphics\Responses.data'), "w", encoding='utf-8')
        File.write(result)
        File.close()

def InitialExecution():
    global personalization_engine, pattern_recognition, predictive_assistance, privacy_mode, reminder_system, reinforcement_learning, system_monitor
    
    set_microphone_status("False")  
    show_text_to_screen("")
    ShowDefaultChatIfNoChats()
    ChatLogIntegration()
    ShowChatsOnGUI()
    
    # Check if contacts database is set up correctly
    ensure_contacts_database()
    
    # Initialize AI modules and track their status
    print("\n=== Initializing AI Modules ===")
    module_status = {
        "pattern_recognition": {"loaded": False, "error": None},
        "predictive_assistance": {"loaded": False, "error": None},
        "privacy_mode": {"loaded": False, "error": None},
        "reinforcement_learning": {"loaded": False, "error": None},
        "reminder_system": {"loaded": False, "error": None}
    }
    
    # Create Data directory if it doesn't exist
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Data")
    os.makedirs(data_dir, exist_ok=True)
    print(f"Data directory verified: {data_dir}")
    
    # Get current timestamp
    current_time = datetime.now().isoformat()
    
    # Initialize pattern recognition
    try:
        pattern_data_path = os.path.join(data_dir, "patterns.json")
        if not os.path.exists(pattern_data_path):
            seed_patterns = {
                "temporal_patterns": {},
                "sequential_patterns": {},
                "contextual_patterns": {},
                "user_preferences": {},
                "interaction_history": [],
                "last_analysis_time": current_time,
                "last_updated": current_time
            }
            with open(pattern_data_path, 'w') as f:
                json.dump(seed_patterns, f, indent=2)
        
        global pattern_recognition
        pattern_recognition = PatternRecognition(user_id=Username, data_path=pattern_data_path)
        module_status["pattern_recognition"]["loaded"] = True
        print("✓ Pattern recognition initialized successfully")
    except Exception as e:
        module_status["pattern_recognition"]["error"] = str(e)
        print(f"✗ Error initializing pattern recognition: {e}")
        pattern_recognition = None
    
    # Initialize privacy mode
    try:
        privacy_data_path = os.path.join(data_dir, "privacy.db")
        privacy_config_path = os.path.join(data_dir, "privacy_config.json")
        
        global privacy_mode
        privacy_mode = PrivacyMode(db_path=privacy_data_path, config_path=privacy_config_path)
        module_status["privacy_mode"]["loaded"] = True
        print("✓ Privacy mode initialized successfully")
    except Exception as e:
        module_status["privacy_mode"]["error"] = str(e)
        print(f"✗ Error initializing privacy mode: {e}")
        privacy_mode = None
    
    # Initialize reinforcement learning
    try:
        rl_data_path = os.path.join(data_dir, "rl_data.json")
        if not os.path.exists(rl_data_path):
            seed_rl_data = {
                "actions_history": [],
                "rewards_history": [],
                "q_values": {},
                "action_counts": {},
                "total_rewards": {},
                "last_updated": current_time
            }
            with open(rl_data_path, 'w') as f:
                json.dump(seed_rl_data, f, indent=2)
        
        global reinforcement_learning
        reinforcement_learning = SimpleReinforcementLearning(
            user_id=Username,
            data_path=rl_data_path,
            strategy=LearningStrategy.EPSILON_GREEDY.value,  # Use enum value
            learning_rate=0.1,
            exploration_rate=0.2
        )
        module_status["reinforcement_learning"]["loaded"] = True
        print("✓ Reinforcement learning initialized successfully")
    except Exception as e:
        module_status["reinforcement_learning"]["error"] = str(e)
        print(f"✗ Error initializing reinforcement learning: {e}")
        reinforcement_learning = None
    
    # Initialize predictive assistance last since it depends on pattern recognition
    try:
        predictive_data_path = os.path.join(data_dir, "predictive_data.json")
        if not os.path.exists(predictive_data_path):
            seed_predictive_data = {
                "suggestions": [],
                "suggestion_responses": [],
                "context_history": [],
                "last_updated": current_time
            }
            with open(predictive_data_path, 'w') as f:
                json.dump(seed_predictive_data, f, indent=2)
        
        global predictive_assistance
        predictive_assistance = SimplePredictiveAssistance(
            user_id=Username,
            pattern_recognition=pattern_recognition,
            data_path=predictive_data_path
        )
        module_status["predictive_assistance"]["loaded"] = True
        print("✓ Predictive assistance initialized successfully")
    except Exception as e:
        module_status["predictive_assistance"]["error"] = str(e)
        print(f"✗ Error initializing predictive assistance: {e}")
        predictive_assistance = None
    
    # Initialize reminder system
    try:
        global reminder_system
        reminder_system = ReminderSystem()
        print("✓ Reminder system initialized successfully")
        module_status["reminder_system"]["loaded"] = True
        
        # Test the reminder system
        reminder_system.add_reminder("Test reminder", datetime.now() + timedelta(seconds=10))
        print("Test reminder added successfully")
    except Exception as e:
        print(f"✗ Error initializing reminder system: {e}")
        module_status["reminder_system"]["loaded"] = False
        module_status["reminder_system"]["error"] = str(e)
        reminder_system = None
    
    # Display module status
    print("\n=== AI Module Status ===")
    for module_name, status in module_status.items():
        if status["loaded"]:
            print(f"✓ {module_name}: Successfully loaded")
        else:
            print(f"✗ {module_name}: Failed to load - {status['error']}")
    
    # Test predictive assistance if available
    if predictive_assistance and module_status["predictive_assistance"]["loaded"]:
        print("\n=== Testing Predictive Assistance ===")
        try:
            current_state = {
                "time": datetime.now().isoformat(),
                "day_of_week": datetime.now().strftime("%A"),
                "hour": datetime.now().hour,
                "location": "home",
                "last_activity": "startup"
            }
            
            predictions = predictive_assistance.get_predictions(current_state)
            print(f"Successfully got {len(predictions)} predictions:")
            for pred in predictions:
                print(f"- {pred.get('title', 'Unknown')} (confidence: {pred.get('confidence', 0):.2f})")
        except Exception as e:
            print(f"Error testing predictions: {e}")
    
    print("\n=== AI Module Initialization Complete ===")
    
    # Notify user of initialization status
    status_message = "AI modules initialized. "
    loaded_modules = [name for name, status in module_status.items() if status["loaded"]]
    failed_modules = [name for name, status in module_status.items() if not status["loaded"]]
    
    if loaded_modules:
        status_message += f"Successfully loaded: {', '.join(loaded_modules)}. "
    if failed_modules:
        status_message += f"Failed to load: {', '.join(failed_modules)}."
    
    show_text_to_screen(f"{Assistantname} : {status_message}")
    TextToSpeech(status_message)

def ensure_contacts_database():
    """Make sure the contacts database is properly set up"""
    db_path = r"F:\jarvis\contacts.db"
    if not os.path.exists(db_path) or os.path.getsize(db_path) < 100:  # Check if file is missing or very small
        print("*with focused determination* Initializing contacts database...")
        try:
            import sqlite3
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            # Create contacts table if it doesn't exist
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS contacts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(200),
                    mobile_no VARCHAR(255),
                    email VARCHAR(255)
                )
            ''')
            
            # Add a test contact if database is empty
            cursor.execute("SELECT COUNT(*) FROM contacts")
            if cursor.fetchone()[0] == 0:
                cursor.execute('''
                    INSERT INTO contacts (name, mobile_no, email)
                    VALUES (?, ?, ?)
                ''', ("Test Contact", "1234567890", "test@example.com"))
                print("*with satisfaction* Successfully added initial contact data")
            
            conn.commit()
            conn.close()
            print("*with pride* Contacts database initialization completed successfully")
        except Exception as e:
            error_msg = f"*with concern* I apologize, sir. I've encountered an issue while setting up the contacts database: {e}"
            print(error_msg)
            TextToSpeech(error_msg)
    else:
        print("*with assurance* Contacts database is properly configured and ready for use, sir")

def check_system_health():
    global system_monitor
    if system_monitor:
        try:
            health_summary = system_monitor.get_system_health_summary()
            status_msg = (
                f"*with professionalism* System health analysis complete, sir. "
                f"Current status: {health_summary['status']}. "
                f"*with precision* CPU utilization is at {health_summary['metrics']['cpu_percent']}%, "
                f"Memory usage stands at {health_summary['metrics']['memory_percent']}%, "
                f"and Storage capacity is at {health_summary['metrics']['disk_percent']}%"
            )
            return status_msg
        except Exception as e:
            return "*with regret* I apologize, sir. I seem to be having trouble accessing the system metrics. The monitoring service might need attention."
    else:
        return "*with concern* Sir, I regret to inform you that the system monitoring module is currently inactive. Shall I attempt to reinitialize it?"

speak_text()
InitialExecution()

def speak_battery_status():
    try:
        battery = psutil.sensors_battery()
        if battery is not None:
            percent = battery.percent
            plugged = battery.power_plugged
            
            # Create a more sophisticated and emotionally expressive message
            if plugged:
                if percent >= 95:
                    status_message = f"*with satisfaction* Sir, your device is fully charged at {percent}%. You may disconnect the power source if you wish."
                else:
                    status_message = f"*with assurance* Sir, your device is currently charging and has reached {percent}% capacity. {Username},sir."
            else:
                if percent > 80:
                    status_message = f"*with confidence* Power levels are optimal,  ({Username},sir.)"
                    status_message = f"*with confidence* Power levels are optimal, sir. Current charge stands at {percent}%."
                elif percent > 50:
                    status_message = f"*with calm* Battery levels are satisfactory at {percent}%,({Username}, sir,)"
                elif percent > 20:
                    status_message = f"*with gentle concern* Sir, I recommend connecting to a power source soon. Battery level is at {percent}%. {Username},sir."
                else:
                    status_message = f"*with urgency* Sir, immediate attention required. Battery level is critically low at {percent}%. Please connect to a power source. {Username},sir."
            
            print(status_message)
            TextToSpeech(status_message)
        else:
            message = "*with regret* I apologize, sir. I'm unable to access the battery information on this device."
            TextToSpeech(message)
    except Exception as e:
        error_msg = f"*with concern* My apologies, sir. I've encountered an error while checking the battery status: {e}"
        print(error_msg)
        TextToSpeech(error_msg)

def monitor_battery_status():
    """Continuously monitor the battery status and announce charging state changes with sophistication."""
    warned_levels = set()  # Keep track of levels already warned to avoid repetition
    previous_plugged_state = None  # Track the previous charging state

    while True:
        try:
            battery = psutil.sensors_battery()
            if battery is not None:
                percent = battery.percent
                plugged = battery.power_plugged

                # Announce charging state changes with personality
                if previous_plugged_state is not None and plugged != previous_plugged_state:
                    if plugged:
                        charging_message = "*with satisfaction* Sir, I've detected that power input has been connected. Charging has commenced."
                    else:
                        charging_message = "*with attentiveness* Sir, I notice the device has been disconnected from power."
                    print(charging_message)
                    TextToSpeech(charging_message)

                previous_plugged_state = plugged

                # Warn at specific thresholds with personality
                if not plugged and percent in [20, 15, 10, 5] and percent not in warned_levels:
                    if percent == 20:
                        warning_message = f"*with gentle concern* Sir, I recommend connecting to power soon. Battery has declined to {percent}%."
                    elif percent == 15:
                        warning_message = f"*with growing concern* Sir, battery levels are becoming concerning at {percent}%. Please consider charging soon."
                    elif percent == 10:
                        warning_message = f"*with urgency* Sir, battery situation is becoming critical at {percent}%. Immediate charging is advised."
                    else:  # 5%
                        warning_message = f"*with high alert* Sir, battery at critical {percent}%! Immediate action required to prevent system shutdown."
                    print(warning_message)
                    TextToSpeech(warning_message)
                    warned_levels.add(percent)
            else:
                message = "*with regret* I apologize, sir. I'm unable to monitor the battery status on this device."
                TextToSpeech(message)

            time.sleep(10)  # Check battery status every 10 seconds
        except Exception as e:
            error_msg = f"*with concern* My apologies, sir. I've encountered an error while monitoring the battery: {e}"
            print(error_msg)
            TextToSpeech(error_msg)
            break

# Start the battery monitoring in a separate thread
battery_thread = threading.Thread(target=monitor_battery_status, daemon=True)
battery_thread.start()

# Add a global variable to track sleep mode
# Global variables
sleep_mode = False
sleep_event = threading.Event()

def load_hand_gesture_module():
    """Dynamically import the hand gesture module"""
    try:
        print("Attempting to load hand gesture module...")
        # Put the import inside a try block so it won't crash the program at startup
        try:
            # First try to import mediapipe which is the dependency
            import mediapipe
            print("MediaPipe imported successfully")
            
            # Only try to import hand_main if mediapipe works
            from Backend.hand_main import (
                Config, cap, detector, mode, active, get_finger_state,
                handle_cursor_mode, handle_scroll_mode, handle_volume_mode, handle_zoom_mode
            )
            print("Hand gesture module loaded successfully")
            
            return {
                "Config": Config, 
                "cap": cap, 
                "detector": detector, 
                "mode": mode, 
                "active": active, 
                "get_finger_state": get_finger_state,
                "handle_cursor_mode": handle_cursor_mode, 
                "handle_scroll_mode": handle_scroll_mode, 
                "handle_volume_mode": handle_volume_mode, 
                "handle_zoom_mode": handle_zoom_mode
            }
        except ImportError as e:
            print(f"Failed to import MediaPipe or hand tracking: {e}")
            print("Hand gesture controls require TensorFlow and MediaPipe.")
            return None
    except Exception as e:
        print(f"Error loading hand gesture module: {e}")
        return None

def start_hand_gesture_module():
    """Start the hand gesture module in a separate thread"""
    try:
        # Dynamically import the hand tracking module
        hand_module = load_hand_gesture_module()
        
        if not hand_module:
            message = "*with regret* Hand gesture module could not be loaded. It might require additional libraries."
            print(message)
            TextToSpeech(message)
            show_text_to_screen(f"{Assistantname} : {message}")
            
            # Try to use basic OpenCV for hand detection as fallback
            try:
                import cv2
                print("Attempting to use basic OpenCV hand detection...")
                
                cap = cv2.VideoCapture(0)
                if not cap.isOpened():
                    error_msg = "*with concern* Could not open webcam."
                    print(error_msg)
                    TextToSpeech(error_msg)
                    return False
                    
                # Use a simple colored object tracking as an extremely basic fallback
                # Detect blue objects as a proxy for hands
                TextToSpeech("*with determination* Starting simplified hand tracking. Try using a blue object.")
                
                while True:
                    ret, frame = cap.read()
                    if not ret:
                        break
                        
                    # Convert to HSV color space
                    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                    
                    # Define blue color range
                    lower_blue = np.array([100, 50, 50])
                    upper_blue = np.array([130, 255, 255])
                    
                    # Create a mask for blue color
                    mask = cv2.inRange(hsv, lower_blue, upper_blue)
                    
                    # Find contours
                    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                    
                    # Draw contours and track largest object
                    if contours:
                        c = max(contours, key=cv2.contourArea)
                        if cv2.contourArea(c) > 500:  # Minimum area threshold
                            x, y, w, h = cv2.boundingRect(c)
                            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                            
                            # Get center of the object
                            center_x = x + w//2
                            center_y = y + h//2
                            
                            # Move mouse cursor based on detected object
                            screen_w, screen_h = p.size()
                            cursor_x = int(center_x * (screen_w/frame.shape[1]))
                            cursor_y = int(center_y * (screen_h/frame.shape[0]))
                            p.moveTo(cursor_x, cursor_y)
                            
                            # Detect clicking action (when object area changes rapidly)
                            cv2.putText(frame, f"Area: {cv2.contourArea(c)}", (10, 30), 
                                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    
                    # Display the result
                    cv2.imshow("Basic Hand Tracking", frame)
                    
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                
                cap.release()
                cv2.destroyAllWindows()
                return True
                
            except Exception as e:
                print(f"Error with basic hand tracking: {e}")
                show_text_to_screen(f"{Assistantname} : *with apology* Sorry, hand tracking is not available.")
                return False
                
            return False
            
        # If hand_module loaded correctly, extract the resources
        Config = hand_module["Config"]
        cap = hand_module["cap"]
        detector = hand_module["detector"]
        mode = hand_module["mode"]
        active = hand_module["active"]
        get_finger_state = hand_module["get_finger_state"]
        handle_cursor_mode = hand_module["handle_cursor_mode"]
        handle_scroll_mode = hand_module["handle_scroll_mode"]
        handle_volume_mode = hand_module["handle_volume_mode"]
        handle_zoom_mode = hand_module["handle_zoom_mode"]
        
        while True:
            success, img = cap.read()
            if not success:
                break

            img = cv2.flip(img, 1)
            img = detector.find_hands(img)
            lmList = detector.find_position(img, draw=False)

            if not lmList:
                mode = 'N'
                active = 0
                continue
            
            if len(lmList) != 0:
                fingers = get_finger_state(lmList)
                
                if active == 0:
                    if fingers == [0, 1, 0, 0, 0]:  # Only index finger extended
                        mode = 'Cursor'
                        active = 1
                    elif fingers == [1, 1, 1, 1, 1]:  # All fingers extended
                        mode = 'Scroll'
                        active = 1
                    elif fingers == [1, 1, 0, 0, 0]:  # Thumb and index extended
                        mode = 'Volume'
                        active = 1
                    elif fingers == [1, 1, 1, 0, 0]:  # Thumb, index, middle extended
                        mode = 'Zoom'
                        active = 1
            
            cv2.rectangle(img, (Config.CURSOR_BOX[0], Config.CURSOR_BOX[1]),
                        (Config.CURSOR_BOX[2], Config.CURSOR_BOX[3]), (255, 0, 0), 2)
            
            if mode == 'Scroll':
                img = handle_scroll_mode(img, lmList, fingers)
            elif mode == 'Volume':
                img = handle_volume_mode(img, lmList, fingers)
            elif mode == 'Cursor':
                img = handle_cursor_mode(img, lmList, fingers)
            elif mode == 'Zoom':
                img = handle_zoom_mode(img, lmList, fingers)
            
            cv2.imshow('Hand Control', img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        return True
    except Exception as e:
        error_msg = f"*with regret* Error in hand gesture module: {str(e)}"
        print(error_msg)
        TextToSpeech(error_msg)
        show_text_to_screen(f"{Assistantname} : {error_msg}")
        return False

def extract_contact_name(query):
    """Extracts the contact name from a call command string and strips punctuation."""
    print(f"Original query: '{query}'")  # Debug log
    
    # Handle video and audio call formats
    keywords = [
        "make video call to", 
        "video call to",
        "make video call", 
        "video call",
        "make audio call to",
        "audio call to",
        "make audio call",
        "audio call",
        "call to", "call",
        "make call to", "make call"
    ]
    
    q = query.lower().strip()
    print(f"Lowercase query: '{q}'")  # Debug log
    
    # First check if this might be a direct short name command
    # Pattern: "make audio call deep" or similar very short patterns
    if any(pattern in q for pattern in ["audio call", "video call"]) and len(q.split()) <= 4:
        # This might be a short command like "make audio call deep"
        # Extract everything after the call type
        if "audio call" in q:
            name = q.replace("make", "").replace("audio", "").replace("call", "").strip()
        elif "video call" in q:
            name = q.replace("make", "").replace("video", "").replace("call", "").strip()
        else:
            name = q.replace("make", "").replace("call", "").strip()
            
        print(f"Extracted short name: '{name}'")
        if name:  # Only return if we found something
            return name.strip(string.punctuation + " ")
    
    # Handle special case for "make video call [name]" without "to"
    if "make video call" in q and "to" not in q:
        name = q.replace("make video call", "").strip()
        print(f"Direct extraction without 'to': '{name}'")  # Debug log
        return name.strip(string.punctuation + " ")
        
    if "video call" in q and "to" not in q:
        name = q.replace("video call", "").strip()
        print(f"Direct extraction without 'to': '{name}'")  # Debug log
        return name.strip(string.punctuation + " ")
    
    # Handle special case for "make audio call [name]" without "to"
    if "make audio call" in q and "to" not in q:
        name = q.replace("make audio call", "").strip()
        print(f"Direct extraction without 'to': '{name}'")  # Debug log
        return name.strip(string.punctuation + " ")
        
    if "audio call" in q and "to" not in q:
        name = q.replace("audio call", "").strip()
        print(f"Direct extraction without 'to': '{name}'")  # Debug log
        return name.strip(string.punctuation + " ")
    
    # Try standard keyword patterns
    for key in keywords:
        if key in q:
            name = q.split(key)[-1].strip()
            print(f"Extracted using keyword '{key}': '{name}'")  # Debug log
            return name.strip(string.punctuation + " ")
            
    # Fallback: try to extract name from the part after "call" or the last word
    if "call" in q:
        parts = q.split("call")
        if len(parts) > 1:
            name = parts[-1].strip()
            print(f"Fallback extraction after 'call': '{name}'")  # Debug log
            return name.strip(string.punctuation + " ")
    
    # Last resort: try to extract the last word if it's not a command word
    command_words = ["make", "audio", "video", "call", "to"]
    words = q.split()
    if words and words[-1] not in command_words:
        name = words[-1]
        print(f"Last resort extraction - last word: '{name}'")
        return name.strip(string.punctuation + " ")
    
    # If no patterns match, just return the original query
    print(f"No patterns matched, returning original: '{query}'")  # Debug log
    return query.strip().strip(string.punctuation + " ")

def parse_command(command: str) -> tuple[str | None, str | None, str | None]:
    """Parse commands like:
    - 'give reply to [name]'
    - 'send a message to [name]'
    - 'send a [message] to [name]'
    - 'send a message [name]'
    
    Returns:
    - tuple(recipient_name, message_content, command_type)
    - command_type is either "reply" or "send"
    """
    try:
        # Log the command for debugging
        print(f"Parsing command: {command}")
        
        # Convert to lowercase for easier matching
        cmd_lower = command.lower().strip()
        
        # Pattern for "give reply to [name]"
        if cmd_lower.startswith("give reply to "):
            name = command[len("give reply to "):].strip()
            return name, None, "reply"
            
        # Pattern for "reply to [name]"
        if cmd_lower.startswith("reply to "):
            name = command[len("reply to "):].strip()
            return name, None, "reply"
        
        # Pattern for "send message to [name]"
        elif cmd_lower.startswith("send a message to "):
            name = command[len("send a message to "):].strip()
            return name, None, "send"
        
        # Pattern for "send [message] to [name]"
        elif " to " in cmd_lower and cmd_lower.startswith("send "):
            parts = cmd_lower.split(" to ", 1)
            message = parts[0][len("send "):].strip()
            name = parts[1].strip()
            return name, message, "send"
        
        # Pattern for "send message [name]"
        elif cmd_lower.startswith("send a message "):
            name = command[len("send a message "):].strip()
            return name, None, "send"
            
        # Fallback regex patterns if the simple string operations don't work
        import re
        pattern_reply = r"give reply to (.+)"
        pattern_reply2 = r"reply to (.+)"
        pattern_send1 = r"send a message to (.+)"
        pattern_send2 = r"send (.+) to (.+)"
        pattern_send3 = r"send a message (.+)"
        
        match_reply = re.match(pattern_reply, command, re.IGNORECASE)
        match_reply2 = re.match(pattern_reply2, command, re.IGNORECASE)
        match_send1 = re.match(pattern_send1, command, re.IGNORECASE)
        match_send2 = re.match(pattern_send2, command, re.IGNORECASE)
        match_send3 = re.match(pattern_send3, command, re.IGNORECASE)
        
        if match_reply:
            return match_reply.group(1).strip(), None, "reply"
        elif match_reply2:
            return match_reply2.group(1).strip(), None, "reply"
        elif match_send1:
            return match_send1.group(1).strip(), None, "send"
        elif match_send2:
            return match_send2.group(2).strip(), match_send2.group(1).strip(), "send"
        elif match_send3:
            return match_send3.group(1).strip(), None, "send"
        
        print(f"Failed to parse command: {command}")
        return None, None, None
        
    except Exception as e:
        print(f"Error parsing command: {str(e)}")
        return None, None, None
def MainExecution():
    global sleep_mode, personalization_engine, pattern_recognition, predictive_assistance, system_monitor, reminder_system
    
    # Initialize current_state with relevant context
    current_state = {
        "time": datetime.now(),
        "day_of_week": datetime.now().strftime("%A"),
        "hour": datetime.now().hour,
        "sleep_mode": sleep_mode
    }
    
    # Initialize TaskExecution and ImageExecution at the start of the function
    TaskExecution = False
    ImageExecution = False  # Initialize ImageExecution to avoid UnboundLocalError
    
    # Check if we're in sleep mode
    if sleep_mode:
        set_assistant_status("Sleeping...")
        Query = SpeechRecognition()
        
        # Only respond to wake up command
        if Query and "wake up" in Query.lower():
            sleep_mode = False
            sleep_event.clear()
            wake_up_message = "*with satisfaction* I'm awake now! How can I assist you? What will you do after waking me up? Will you make tea for me or get it made for me?"
            show_text_to_screen(f"{Assistantname} : {wake_up_message}")
            TextToSpeech(wake_up_message)
            return True
        return False
    
    # Normal operation
    set_assistant_status("Listening...")
    
    # First try to get voice input
    Query = SpeechRecognition()
    is_text_query = False
    
    # If we got voice input, modify it
    if Query:
        Query = query_modifier(Query)
    else:
        # If no voice input, set is_text_query to True since we'll be handling text commands
        is_text_query = True
    
    if not Query:
        return False
    
    # Log command for debugging
    if is_text_query:
        print(f"\n=== TEXT COMMAND RECEIVED: '{Query}' ===")
    else:
        print(f"\n=== VOICE COMMAND RECEIVED: '{Query}' ===")
        
    show_text_to_screen(f"{Username} : {Query}")
    set_assistant_status("Thinking...")

    # --- ADVANCED TODO QUERY ROUTING ---
    # Use QueryManager to check if this is a supported advanced todo command
    qm = QueryManager()
    todo_commands = qm.parse_query(Query)
    if todo_commands and personalization_engine:
        print(f"Routing to advanced todo system: {todo_commands}")
        response = personalization_engine.process_query_with_manager(Query)
        show_text_to_screen(f"{Assistantname} : {response}")
        TextToSpeech(response)
        return True

    # Check for reminder display commands
    if any(phrase in Query.lower() for phrase in ["show reminders", "show daily reminders", "show today reminders", "show all reminders", "what are my reminders", "list reminders", "display reminders", "so reminders", "so what are my reminders","so daily reminders","so today reminders","so all reminders","so what are my reminders","so list reminders","so display reminders"]):
        print("DEBUG: Show reminders command recognized!")
        if reminder_system:
            try:
                # Determine which reminders to show based on the query
                timeframe = "all"  # Default to showing all reminders
                if "today" in Query.lower():
                    timeframe = "today"
                elif "daily" in Query.lower():
                    timeframe = "daily"
                elif "tomorrow" in Query.lower():
                    timeframe = "tomorrow"
                
                # Get the reminders for the specified timeframe
                response = reminder_system.get_reminders(timeframe)
                show_text_to_screen(f"{Assistantname} : {response}")
                TextToSpeech(response)
                return True
            except Exception as e:
                error_msg = f"*with regret* I'm sorry, I couldn't show your reminders. Error: {e}"
                show_text_to_screen(f"{Assistantname} : {error_msg}")
                TextToSpeech(error_msg)
                print(f"Error showing reminders: {e}")
                return True
        else:
            error_msg = "*with concern* I'm sorry, the reminder system is not available right now."
            show_text_to_screen(f"{Assistantname} : {error_msg}")
            TextToSpeech(error_msg)
            return True
    
    # Check for message commands first
    if any(phrase in Query.lower() for phrase in ["give reply to", "send a message to", "send a message", "reply to"]):
        try:
            # Parse the command to get recipient name and message type
            recipient_name, message_content, command_type = parse_command(Query)
            
            if not recipient_name:
                error_msg = "*with concern* I couldn't understand who to send the message to. Please try again with a clear contact name."
                show_text_to_screen(f"{Assistantname} : {error_msg}")
                TextToSpeech(error_msg)
                return True
                
            # Get recipient's number
            recipient_number = get_contact_number(recipient_name)
            if not recipient_number:
                error_msg = f"*with regret* I couldn't find a contact named {recipient_name}. Please make sure the contact exists."
                show_text_to_screen(f"{Assistantname} : {error_msg}")
                TextToSpeech(error_msg)
                return True
            
            # Initialize WhatsApp assistant
            assistant = WhatsAppGroqAssistant()
            
            # Handle message content based on command type
            if command_type == "reply":
                # For "give reply to [name]", generate AI response
                prompt_msg = "*with curiosity* What would you like me to reply about?"
                show_text_to_screen(f"{Assistantname} : {prompt_msg}")
                TextToSpeech(prompt_msg)
                prompt = SpeechRecognition()
                
                if not prompt:
                    error_msg = "*with regret* I didn't receive a prompt for the reply. Please try again."
                    show_text_to_screen(f"{Assistantname} : {error_msg}")
                    TextToSpeech(error_msg)
                    return True
                    
                message_to_send = assistant.generate_message(prompt)
                confirm_msg = f"*with satisfaction* I've generated this reply:\n{message_to_send}\nShould I send it?"
                show_text_to_screen(f"{Assistantname} : {confirm_msg}")
                TextToSpeech("*with assurance* I've generated a reply. Should I send it?")
                
            else:  # command_type == "send"
                if not message_content:
                    # Ask for message content
                    prompt_msg = "*with curiosity* What message would you like to send?"
                    show_text_to_screen(f"{Assistantname} : {prompt_msg}")
                    TextToSpeech(prompt_msg)
                    message_content = SpeechRecognition()
                    
                    if not message_content:
                        error_msg = "*with regret* I didn't receive a message to send. Please try again."
                        show_text_to_screen(f"{Assistantname} : {error_msg}")
                        TextToSpeech(error_msg)
                        return True
                
                message_to_send = message_content
                confirm_msg = f"*with assurance* Should I send this message to {recipient_name}:\n{message_to_send}"
                show_text_to_screen(f"{Assistantname} : {confirm_msg}")
                TextToSpeech("*with assurance* Should I send this message?")
            
            # Get confirmation
            confirm_prompt = "*with anticipation* Please say yes to confirm or no to cancel"
            show_text_to_screen(f"{Assistantname} : {confirm_prompt}")
            TextToSpeech(confirm_prompt)
            confirmation = SpeechRecognition()
            
            if confirmation and any(word in confirmation.lower() for word in ["yes", "yeah", "sure", "okay", "send it"]):
                # Send the message
                if assistant.send_whatsapp_message(recipient_number, message_to_send):
                    success_msg = f"*with satisfaction* Message sent successfully to {recipient_name}"
                    show_text_to_screen(f"{Assistantname} : {success_msg}")
                    TextToSpeech(success_msg)
                else:
                    error_msg = f"*with regret* Failed to send message to {recipient_name}. Please try again."
                    show_text_to_screen(f"{Assistantname} : {error_msg}")
                    TextToSpeech(error_msg)
            
            return True
            
        except Exception as e:
            error_msg = f"*with regret* Error processing message command: {str(e)}"
            print(error_msg)
            show_text_to_screen(f"{Assistantname} : *with apology* Sorry, I encountered an error while trying to send the message.")
            TextToSpeech("*with apology* Sorry, I encountered an error while trying to send the message.")
            return True

    # Check for system status request
    if any(keyword in Query.lower() for keyword in ["system status", "system health", "system monitor", "check system"]):
        status = check_system_health()
        TextToSpeech(status)
        show_text_to_screen(f"{Assistantname} : {status}")
        return True
    
    # Track user interaction in personalization engine if available
    if personalization_engine:
        try:
            personalization_engine.track_interaction("query", {"text": Query})
        except Exception as e:
            print(f"Error tracking interaction: {e}")
    
    # Track interaction in pattern recognition system
    if pattern_recognition:
        try:
            # Record this interaction for pattern analysis
            pattern_recognition.add_interaction({
                "activity_type": "voice_command",
                "query": Query,
                "timestamp": datetime.now().isoformat()
            })
        except Exception as e:
            print(f"Error adding to pattern recognition: {e}")
    
    # Get predictive suggestions if available
    predictive_suggestions = []
    if predictive_assistance and not Query:  # Only suggest when user hasn't explicitly asked
        try:
            predictive_suggestions = predictive_assistance.get_predictions(current_state)
            if predictive_suggestions:
                top_suggestion = predictive_suggestions[0]
                suggestion_id = top_suggestion.get('suggestion_id', 'unknown')
                suggestion_msg = f"*with observation* I notice it's {datetime.now().strftime('%A %H:%M')}. Would you like to {top_suggestion.get('title', 'do something')}?"
                show_text_to_screen(f"{Assistantname} : {suggestion_msg}")
                TextToSpeech(suggestion_msg)
                
                # Wait for user response to the suggestion
                response = SpeechRecognition()
                if response and any(word in response.lower() for word in ["yes", "sure", "okay", "fine", "good"]):
                    # User accepted the suggestion
                    if predictive_assistance:
                        predictive_assistance.record_suggestion_response(suggestion_id, True)
                    accept_msg = "*with satisfaction* Great, I'll help you with that."
                    show_text_to_screen(f"{Assistantname} : {accept_msg}")
                    TextToSpeech(accept_msg)
                else:
                    # User rejected or didn't respond clearly
                    if predictive_assistance:
                        predictive_assistance.record_suggestion_response(suggestion_id, False)
                
                TaskExecution = True
        except Exception as e:
            print(f"Error getting predictive suggestions: {e}")
    
    # Check for debug/test commands directly
    if "test call" in Query.lower():
        test_msg = "*with curiosity* This is a test call command pattern. What contact would you like to call?"
        show_text_to_screen(f"{Assistantname} : {test_msg}")
        TextToSpeech(test_msg)
        return True
    
    Decision = FirstLayerDMM(Query)
    
    # Print Decision for debugging
    print("Decision tree from voice command:")
    for d in Decision:
        print(f"  - {d}")
        
    # Debug audio call request specifically
    if "audio call" in Query.lower() or "make audio call" in Query.lower():
        print("DEBUG: Audio call detected in raw query")
        print(f"DEBUG: Exact query: '{Query}'")
        
        # Extract contact name directly for debugging
        contact_name = extract_contact_name(Query)
        print(f"DEBUG: Extracted contact name: '{contact_name}'")
        
        # Try direct call for debugging
        if contact_name:
            print(f"DEBUG: Attempting direct call to {contact_name}")
            try:
                call_result = make_call(contact_name, "audio")
                print(f"DEBUG: Direct call result: {call_result}")
                msg = f"*with satisfaction* Debugging: Made direct audio call to {contact_name}"
                show_text_to_screen(f"{Assistantname} : {msg}")
                # TextToSpeech(msg)
                return True
            except Exception as e:
                print(f"DEBUG: Direct call error: {e}")
    
    # Check for hand gesture module activation
    if any(phrase in Query.lower() for phrase in ["turn on hand gesture", "activate hand gesture", "enable hand gesture", 
                                             "start hand gesture", "control with hand", "use hand gestures"]):
        print("DEBUG: Hand gesture control activation recognized!")
        try:
            hand_gesture_thread = threading.Thread(target=start_hand_gesture_module, daemon=True)
            hand_gesture_thread.start()
            response = "*with satisfaction* Hand gesture module activated. You can now control your computer with hand gestures."
            show_text_to_screen(f"{Assistantname} : {response}")
            TextToSpeech(response)
            return True
        except Exception as e:
            print(f"Error starting hand gesture module: {e}")
            error_msg = "*with regret* I couldn't activate hand gestures. This feature requires additional libraries."
            show_text_to_screen(f"{Assistantname} : {error_msg}")
            TextToSpeech(error_msg)
            return True
    
    # Check for emotion detection activation
    if any(phrase in Query.lower() for phrase in ["detect emotion", "emotion detection", "start emotion detection", 
                                              "how am i feeling", "detect my emotions", "recognize my emotions", 
                                              "analyze my emotions", "check my emotions"]):
        print("DEBUG: Emotion detection command recognized!")
        emotion_thread = threading.Thread(target=start_emotion_detection, daemon=True)
        emotion_thread.start()
        response = "*with assurance* Emotion detection activated. Press 'q' to stop."
        show_text_to_screen(f"{Assistantname} : {response}")
        TextToSpeech(response)
        return True
    
    # Check for reminder-related commands
    if any(phrase in Query.lower() for phrase in ["set reminder", "remind me to", "create reminder", 
                                              "add reminder", "daily reminder", "new reminder",
                                              "show reminders", "show daily reminders", "show today reminders",
                                              "show all reminders", "what are my reminders", "list reminders", "so reminders", ]):
        if any(phrase in Query.lower() for phrase in ["show reminders", "show daily reminders", "show today reminders", "show all reminders", "what are my reminders", "list reminders", "display reminders"]):
            print("DEBUG: Show reminders command recognized!")
            if reminder_system:
                try:
                    # Determine which reminders to show based on the query
                    timeframe = "all"  # Default to showing all reminders
                    if "today" in Query.lower():
                        timeframe = "today"
                    elif "daily" in Query.lower():
                        timeframe = "daily"
                    elif "tomorrow" in Query.lower():
                        timeframe = "tomorrow"
                    
                    # Get the reminders for the specified timeframe
                    response = reminder_system.get_reminders(timeframe)
                    show_text_to_screen(f"{Assistantname} : {response}")
                    TextToSpeech(response)
                    return True
                except Exception as e:
                    error_msg = f"*with regret* I'm sorry, I couldn't show your reminders. Error: {e}"
                    show_text_to_screen(f"{Assistantname} : {error_msg}")
                    TextToSpeech(error_msg)
                    print(f"Error showing reminders: {e}")
                    return True
            else:
                error_msg = "*with concern* I'm sorry, the reminder system is not available right now."
                show_text_to_screen(f"{Assistantname} : {error_msg}")
                TextToSpeech(error_msg)
                return True
        else:
            try:
                # Process the reminder command using the reminder system
                response = reminder_system.set_reminder(Query)
                
                show_text_to_screen(f"{Assistantname} : {response}")
                TextToSpeech(response)
                return True
            except Exception as e:
                error_msg = f"*with regret* I'm sorry, I couldn't process the reminder command. Error: {e}"
                show_text_to_screen(f"{Assistantname} : {error_msg}")
                TextToSpeech(error_msg)
                print(f"Error processing reminder command: {e}")
                return True
    
    # Check for privacy-related commands
    if any(phrase in Query.lower() for phrase in ["privacy mode", "change privacy", "privacy settings", 
                                              "set privacy", "privacy level"]):
        print("DEBUG: Privacy mode command recognized!")
        if privacy_mode:
            try:
                # Handle privacy level commands
                if "high" in Query.lower():
                    privacy_mode.set_privacy_level(privacy_mode.PrivacyLevel.HIGH)
                    response = "*with assurance* Privacy level set to high. Maximum privacy enabled."
                elif "medium" in Query.lower():
                    privacy_mode.set_privacy_level(privacy_mode.PrivacyLevel.MEDIUM)
                    response = "*with assurance* Privacy level set to medium. Balanced privacy settings enabled."
                elif "low" in Query.lower():
                    privacy_mode.set_privacy_level(privacy_mode.PrivacyLevel.LOW)
                    response = "*with assurance* Privacy level set to low. Standard privacy settings enabled."
                else:
                    # Display current privacy settings
                    settings = privacy_mode.get_current_settings()
                    response = f"*with assurance* Current privacy level is {settings['privacy_level']}. Say 'set privacy high', 'medium', or 'low' to change it."
                    
                show_text_to_screen(f"{Assistantname} : {response}")
                TextToSpeech(response)
                return True
            except Exception as e:
                error_msg = f"*with regret* I'm sorry, I couldn't change privacy settings. Error: {e}"
                show_text_to_screen(f"{Assistantname} : {error_msg}")
                TextToSpeech(error_msg)
                print(f"Error changing privacy settings: {e}")
                return True
        else:
            error_msg = "*with concern* I'm sorry, the privacy mode module is not available right now."
            show_text_to_screen(f"{Assistantname} : {error_msg}")
            TextToSpeech(error_msg)
            return True
    
    # Check for personalization-related commands
    if any(phrase in Query.lower() for phrase in ["show suggestions", "to suggestions",  "personalized suggestions", 
                                              "what do you recommend", "any recommendations", 
                                              "what should i do", "suggest something"]):
        print("DEBUG: Personalization suggestion request recognized")
        
        suggestions = []
        
        # Get suggestions from personalization engine
        if personalization_engine:
            try:
                time_suggestions = personalization_engine.get_current_time_suggestions()
                if time_suggestions:
                    suggestions.extend(time_suggestions)
            except Exception as e:
                print(f"Error getting time-based suggestions: {e}")
        
        # Get suggestions from predictive assistance
        if predictive_assistance:
            try:
                predictive_suggestions = predictive_assistance.get_predictions(current_state)
                if predictive_suggestions:
                    suggestions.extend(predictive_suggestions)
            except Exception as e:
                print(f"Error getting predictive suggestions: {e}")
        
        if suggestions:
            # Format suggestions into a readable message
            suggestion_items = []
            for i, sugg in enumerate(suggestions[:3], 1):
                activity = sugg.get('activity_type', sugg.get('title', 'something'))
                confidence = sugg.get('confidence', 0) * 100
                details = sugg.get('details', {})
                description = sugg.get('description', '')
                
                suggestion_text = f"{i}. {activity}"
                if description:
                    suggestion_text += f" - {description}"
                suggestion_text += f" ({confidence:.0f}% confidence)"
                
                suggestion_items.append(suggestion_text)
            
            suggestions_text = "\n".join(suggestion_items)
            response = f"*with assurance* Here are my suggestions based on your patterns and the current time:\n{suggestions_text}"
        else:
            response = "*with concern* I don't have enough data yet to make personalized suggestions. Keep interacting with me!"
            
        show_text_to_screen(f"{Assistantname} : {response}")
        TextToSpeech(response)
        return True
    
    # Check for sleep command
    for query in Decision:
        if any(phrase in query.lower() for phrase in ["go to sleep", "going to sleep", "sleep now", "now sleep jarvis"]):
            sleep_mode = True
            sleep_event.set()
            sleep_message = "with determination I go to sleep, but my heart will stay awake thinking about you!!. Say 'wake up' when you need me."
            show_text_to_screen(f"{Assistantname} : {sleep_message}")
            TextToSpeech(sleep_message)
            return True
    
    # Check for direct call command
    if "direct call" in Query.lower() or "direct phone call" in Query.lower() or "phone call" in Query.lower():
        print("Processing direct phone call command...")
        # Extract contact name
        if "to" in Query.lower():
            contact_name = Query.lower().split("to")[-1].strip()
        else:
            # Try to extract name after "call"
            if "call" in Query.lower():
                contact_name = Query.lower().split("call")[-1].strip()
            else:
                contact_name = ""
                
        print(f"Extracted contact name for direct call: '{contact_name}'")
        
    
    # Rest of your normal processing...

    for queries in Decision:
        if "image to pdf" in queries.lower():
            print("Processing 'image to pdf' command...")
            response = convert_image_to_pdf()
            show_text_to_screen(f"{Assistantname} : {response}")
            TextToSpeech(response)
            TaskExecution = True
            break  # Exit the loop after handling the command
    
    for queries in Decision:
        if "battery" in queries.lower() or "power charging" in queries.lower():
            print("Processing battery status command...")
            speak_battery_status()
            TaskExecution = True
            break  # Exit the loop after handling the command
    
    # Handle video calls only
    
    for queries in Decision:
        # Log the exact query being processed for debugging
        print(f"Examining query for call patterns: '{queries}'")
        
        # Check if this is actually a call-related decision
        if "call" in queries.lower():
            print(f"DEBUG: Found call-related decision: '{queries}'")
            
        # Add audio call patterns alongside video call patterns
        video_call_patterns = ["video call", "make video call"]
        audio_call_patterns = ["audio call", "make audio call"]
        
        # Add debug prints for pattern matching
        if any(pattern in queries.lower() for pattern in video_call_patterns):
            print("MATCHED VIDEO CALL PATTERN")
        if any(pattern in queries.lower() for pattern in audio_call_patterns):
            print("MATCHED AUDIO CALL PATTERN")
        
        # Check for direct audio or video call commands from FirstLayerDMM
        if queries.startswith("audio call") or queries.startswith("make audio call"):
            print("Processing audio call command directly...")
            # Extract the contact name from the command
            if queries.startswith("audio call"):
                contact_name = queries.replace("audio call", "").strip()
            else:
                contact_name = queries.replace("make audio call", "").strip()
                
            print(f"Direct contact name extraction: '{contact_name}'")
            
            if not contact_name:
                # Try extracting using the detailed function
                contact_name = extract_contact_name(queries)
                print(f"Fallback contact extraction: '{contact_name}'")
            
            # Check if contact_name is empty
            if not contact_name or contact_name.strip() == "":
                response = "*with concern* I couldn't understand the contact name. Please try again by saying 'audio call to John' or similar."
                show_text_to_screen(f"{Assistantname} : {response}")
                TextToSpeech(response)
                TaskExecution = True
                break
                
            # Tell user we're processing
            processing_msg = f"*with assurance* Going to audio call with {contact_name}"
            show_text_to_screen(f"{Assistantname} : {processing_msg}")
            TextToSpeech(processing_msg)
            
            # Try WhatsApp call
            try:
                whatsapp_success = make_call(contact_name, "audio")
                
                if whatsapp_success:
                    success_msg = f"*with satisfaction* Going to audio call with {contact_name}"
                    show_text_to_screen(f"{Assistantname} : {success_msg}")
                    print(f"make_call function executed successfully for {contact_name}")
                else:
                    fail_msg = f"*with regret* I couldn't make the audio call to {contact_name}. Please check if the contact exists or try again later."
                    show_text_to_screen(f"{Assistantname} : {fail_msg}")
                    TextToSpeech(fail_msg)
            except Exception as e:
                error_msg = f"*with regret* Error making call: {e}. Please make sure WhatsApp is properly installed."
                show_text_to_screen(f"{Assistantname} : {error_msg}")
                TextToSpeech(error_msg)
                print(f"Error making call: {e}")
                
            TaskExecution = True
            break
            
        # Check for video calls using the original code
        if any(pattern in queries.lower() for pattern in video_call_patterns):
            print("Processing video call command...")
            # Extract the contact name from the query using the new function
            contact_name = extract_contact_name(queries)
            print(f"Extracted contact name: '{contact_name}'")  # Debug log
            
            # Check if contact_name is empty
            if not contact_name or contact_name.strip() == "":
                response = "*with concern* I couldn't understand the contact name. Please try again by saying 'video call to John' or similar."
                show_text_to_screen(f"{Assistantname} : {response}")
                TextToSpeech(response)
                TaskExecution = True
                break
                
            # Tell user we're processing
            processing_msg = f"*with assurance* Going to video call with {contact_name}"
            show_text_to_screen(f"{Assistantname} : {processing_msg}")
            TextToSpeech(processing_msg)
            
            # Try WhatsApp call
            try:
                whatsapp_success = make_call(contact_name, "video")
                
                if whatsapp_success:
                    success_msg = f"*with satisfaction* Going to video call with {contact_name}"
                    show_text_to_screen(f"{Assistantname} : {success_msg}")
                    print(f"make_call function executed successfully for {contact_name}")
                else:
                    fail_msg = f"*with regret* I couldn't make the video call to {contact_name}. Please check if the contact exists or try again later."
                    show_text_to_screen(f"{Assistantname} : {fail_msg}")
                    TextToSpeech(fail_msg)
            except Exception as e:
                error_msg = f"*with regret* Error making call: {e}. Please make sure WhatsApp is properly installed."
                show_text_to_screen(f"{Assistantname} : {error_msg}")
                TextToSpeech(error_msg)
                print(f"Error making call: {e}")                    
                
                
            TaskExecution = True
            break  # Exit the loop after handling the command
            
            TaskExecution = True
            break  # Exit the loop after handling the command
    
    G = any([i for i in Decision if i.startswith("general")])
    R = any([i for i in Decision if i.startswith("realtime")])                      
    
    I = any([i for i in Decision if i.startswith("instagram")])  # Check for Instagram commands

    Mearged_query = " and ".join(
        [" ".join(i.split()[1:]) for i in Decision if i.startswith("general") or i.startswith("realtime")]
        )
    
    for queries in Decision:
        if "generate" in queries:
            ImageGenerationQuery = str(queries)
            ImageExecution = True  # Set ImageExecution to True
            
    for queries in Decision:
        if TaskExecution == False:
            if any(queries.startswith(func) for func in Functions):
                run(Automation(list(Decision)))
                TaskExecution = True
                
    # Handle Instagram commands
    if I and TaskExecution == False:
        print("Processing Instagram command...")
        # Pass Instagram commands to Automation
        instagram_commands = [q for q in Decision if q.startswith("instagram")]
        if instagram_commands:
            run(Automation(instagram_commands))
            TaskExecution = True
                
    if ImageExecution == True:
        with open(r"Frontend\Files\ImageGeneration.data", "w") as file:
            file.write(f"{ImageGenerationQuery}, True")

        try:  
            p1 = subprocess.Popen(['python', r'Backend\ImageGeneration.py'],
                                  stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                  stdin=subprocess.PIPE, shell=False)
            subprocesses.append(p1)
            _, stderr = p1.communicate()  # Wait for the process to complete
            if stderr:
                    print(f"Error in ImageGeneration.py: {stderr.decode()}")
        except Exception as e:
            print(f"Error starting ImageGeneration.py: {e}")
                
    if G and R or R:
        
        set_assistant_status("Searching...")
        Answer = RealtimeSearchEngine(query_modifier(Mearged_query))
        show_text_to_screen(f" {Assistantname} : {Answer}")
        set_assistant_status("Answering...")
        TextToSpeech(Answer)
        return True
    
    else:
        for Queries in Decision:
             
            if "general" in Queries:
                set_assistant_status("Thinking...")
                QueryFinal = Queries.replace("general ","")
                Answer = Chatbot (query_modifier (QueryFinal))
                show_text_to_screen(f" {Assistantname} : {Answer}")
                set_assistant_status("Answering...")
                TextToSpeech(Answer)
                return True
             
            elif "realtime" in Queries:
                set_assistant_status("Searching...")
                QueryFinal = Queries.replace("realtime ","")
                Answer = RealtimeSearchEngine (query_modifier (QueryFinal))
                show_text_to_screen(f" {Assistantname} : {Answer}")
                set_assistant_status("Answering...")
                TextToSpeech(Answer)
                return True
            
            elif "exit" in Queries:
                QueryFinal = "*with determination* Okay, Bye!"
                Answer = Chatbot (query_modifier (QueryFinal))
                show_text_to_screen(f" {Assistantname} : {Answer}")
                set_assistant_status("Answering...")
                TextToSpeech(Answer)
                set_assistant_status("Answering...")
                os._exit(1)
            
            # Instagram queries are now handled above
            elif "instagram" in Queries:
                print(f"Instagram query detected: {Queries}")
                # This is now handled in the dedicated Instagram section above
                pass


def FirstThread():
    MainExecution()
    while True:
        try:
            CurrentStatus = get_microphone_status()

            if CurrentStatus == "True":
                MainExecution()
            else:
                AIStatus = get_microphone_status()

                if "Available... " in AIStatus:
                    sleep(0.1)
                else:
                    set_assistant_status("Available...")
        except Exception as e:
            print(f"Error in FirstThread: {e}")
            sleep(1)

def SecondThread():

    graphical_user_interface()

def find_whatsapp_path():
    """Try to find WhatsApp installation path"""
    possible_paths = [
        os.path.expandvars(r"%LocalAppData%\WhatsApp\WhatsApp.exe"),
        os.path.expandvars(r"%LocalAppData%\Programs\WhatsApp\WhatsApp.exe"),
        r"C:\Program Files\WindowsApps\WhatsAppDesktop_*\WhatsApp.exe",
        r"C:\Program Files\WhatsApp\WhatsApp.exe",
        r"C:\Program Files (x86)\WhatsApp\WhatsApp.exe",
        os.path.expandvars(r"%ProgramFiles%\WhatsApp\WhatsApp.exe"),
        os.path.expandvars(r"%ProgramFiles(x86)%\WhatsApp\WhatsApp.exe"),
    ]
    
    # First check exact paths
    for path in possible_paths:
        if not path.endswith("*") and os.path.exists(path):
            return path
            
    # Then check paths with wildcards
    for path in possible_paths:
        if "*" in path:
            import glob
            matches = glob.glob(path)
            if matches:
                return matches[0]
                
    # Try registry as last resort
    try:
        import winreg
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\WhatsApp.exe") as key:
            path = winreg.QueryValue(key, None)
            if os.path.exists(path):
                return path
    except:
        pass
        
    return None

def make_call(contact_name, call_type="audio"):
    """Make a WhatsApp call (audio or video) to a contact"""
    try:
        # Initialize WhatsApp assistant
        assistant = WhatsAppGroqAssistant()
        
        # Check internet connection
        if not assistant.check_internet():
            error_msg = "*with concern* No internet connection available"
            print(error_msg)
            return False
            
        # Get contact number
        number = get_contact_number(contact_name)
        if not number:
            error_msg = f"*with regret* Contact {contact_name} not found"
            print(error_msg)
            return False
        
        # Clean the phone number - remove country codes like +91 and non-digit characters
        number = clean_phone_number(number)
        print(f"Cleaned phone number: {number}")  # Debug log
            
        # Try to open WhatsApp Desktop app using the existing function
        if not open_whatsapp_app():
            error_msg = "*with concern* WhatsApp Desktop app not found. Please install it from the Microsoft Store."
            print(error_msg)
            return False
            
        # Find and activate WhatsApp window
        whatsapp_window = None
        for _ in range(5):  # Try multiple times to find WhatsApp window
            try:
                import pyautogui
                whatsapp_window = pyautogui.getWindowsWithTitle("WhatsApp")
                if whatsapp_window:
                    break
            except:
                pass
            time.sleep(1)
            
        if not whatsapp_window:
            error_msg = "*with concern* WhatsApp window not found. Please ensure it's open and visible."
            print(error_msg)
            return False
            
        whatsapp_window[0].activate()
        time.sleep(2)  # Wait for window to be active
        
        # Use keyboard shortcut to focus search
        pyautogui.hotkey('ctrl', 'f')
        time.sleep(1)
        
        # Type phone number
        pyautogui.write(number)
        time.sleep(2)
        
        # Select contact
        pyautogui.press('down')  # Navigate to the contact
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(2)
        
        # Navigate to call button with more robust tab navigation
        tab_count = 11 if call_type == "audio" else 10
        for i in range(tab_count):
            pyautogui.press('tab')
            time.sleep(0.5)  # Increased wait time between tabs
            
        # Initiate call
        pyautogui.press('enter')
        
        print(f"Initiating {call_type} call to {contact_name}")
        return True
        
    except Exception as e:
        print(f"Error making call: {e}")
        print("Please ensure WhatsApp window is visible and not minimized")
        print("Also ensure the window is in focus and not covered by other windows")
        return False

def clean_phone_number(number):
    """Remove country codes and special characters from phone number"""
    # Remove common country codes
    country_codes = ['+91', '+1', '+44', '+86', '+81', '+49', '+33', '+7', '+61']
    
    for code in country_codes:
        if number.startswith(code):
            number = number[len(code):]  # Remove the country code
            break
    
    # Remove any non-digit characters (spaces, dashes, parentheses, etc.)
    import re
    number = re.sub(r'\D', '', number)
    
    return number
    

if __name__ == "__main__":
    
    # Initialize reminder system
    reminder_system = ReminderSystem()
    
    # Your existing threads
    thread2 = threading.Thread(target=FirstThread, daemon=True)
    thread2.start()
    SecondThread()
    thread1 = threading.Thread(target=SecondThread, daemon=True)
    thread1.start()
    