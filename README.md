# 🤖 Jarvis AI Assistant - Advanced Personal Digital Assistant

<div align="center">
  <h1>🚀 Jarvis AI Assistant v1.0.0</h1>
  <p>A comprehensive AI-powered personal assistant combining computer vision, voice interaction, automation, and machine learning capabilities</p>
  
  [![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
  [![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
  [![OpenCV](https://img.shields.io/badge/OpenCV-4.8%2B-brightgreen)](https://opencv.org/)
  [![Groq API](https://img.shields.io/badge/Groq-API-orange)](https://groq.com/)
  [![Status](https://img.shields.io/badge/status-active-success)](https://github.com/yourusername/jarvis)
</div>

## 🌟 Features Overview

### 🧠 AI & Natural Language Processing
- **Advanced Chat Interface**: Powered by Groq API for intelligent conversations
- **Voice Recognition**: Real-time speech-to-text with multiple language support
- **Text-to-Speech**: Natural voice synthesis with customizable voices
- **Pattern Recognition**: Machine learning-based user behavior analysis
- **Predictive Assistance**: AI-powered suggestions based on user habits
- **Personalization Engine**: Adaptive learning from user interactions

### 👁️ Computer Vision & Recognition
- **Facial Recognition**: Real-time face detection and recognition using OpenCV
- **Emotion Detection**: Analyze facial expressions and emotional states
- **Object Detection**: Identify and classify objects in real-time
- **Hand Gesture Control**: Control computer with hand gestures using MediaPipe
- **Training Mode**: Add new faces to the recognition system

### 📱 Communication & Integration
- **WhatsApp Integration**: Send messages and make calls through WhatsApp
- **Contact Management**: SQLite-based contact database
- **Voice/Video Calling**: Make audio and video calls to contacts
- **Message Generation**: AI-powered message composition and replies
- **Instagram Integration**: Social media automation capabilities

### ⚙️ System Automation & Monitoring
- **System Health Monitoring**: CPU, memory, disk, and battery tracking
- **Battery Status**: Real-time battery level monitoring and notifications
- **File Operations**: Convert images to PDF, file management
- **Application Control**: Open/close applications, system commands
- **Reminder System**: Task scheduling and reminder management
- **Auto-updater**: Automatic software updates and maintenance

### 🔒 Privacy & Security
- **End-to-End Encryption**: Secure communications and data protection
- **Privacy Modes**: Multiple privacy levels (High, Medium, Low)
- **Secure Key Storage**: Protected API keys and sensitive data
- **Data Anonymization**: User data protection and anonymization

### 🎨 Modern User Interface
- **Dark Theme GUI**: Modern PyQt5-based interface with dark theme
- **Real-time Status**: Live system status and activity indicators
- **Chat Interface**: Intuitive chat-based interaction
- **Settings Panel**: Comprehensive configuration options
- **Accessibility Features**: Screen reader support and keyboard navigation

## 🚀 Quick Start

### 📋 Prerequisites
- **Python 3.8+** (Required)
- **Windows 10/11** (Primary support)
- **Webcam** (For facial recognition and gesture control)
- **Microphone** (For voice interaction)
- **Internet Connection** (For AI features and updates)

### 🛠️ Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/jarvis-ai-assistant.git
   cd jarvis-ai-assistant
   ```

2. **Install Dependencies** (Automatic)
   ```bash
   python install_dependencies.py
   ```
   
   Or manually:
   ```bash
   pip install -r Requirements.txt
   ```

3. **Set Up Environment Variables**
   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   # Add other API keys as needed
   ```

4. **Initialize Required Directories**
   The application will automatically create necessary directories:
   - `Backend/Data/` - User data and personalization
   - `Backend/config/` - Configuration files
   - `logs/` - System logs
   - `generated_code/` - AI-generated code
   - `generated_images/` - AI-generated images

### 🎯 First Run

1. **Launch Jarvis**
   ```bash
   python Main.py
   ```

2. **Set Up Facial Recognition** (Optional)
   - Add face images to `Backend/samples/` directory
   - Name them as `face.[ID].1.jpg` (e.g., `face.john.1.jpg`)
   - Or use legacy format: `known_person.jpg`, `known_person2.jpg`

3. **Configure Voice Settings**
   - Test microphone and speakers
   - Adjust voice recognition sensitivity
   - Set preferred text-to-speech voice

## 📁 Project Structure

```
jarvis-ai-assistant/
├── 🎯 Main.py                    # Main application entry point
├── 📦 install_dependencies.py    # Automatic dependency installer
├── 📋 Requirements.txt          # Python dependencies
├── 📄 README.md                 # This documentation
├── 🔧 version.json              # Version information
├── 📱 facial_recognition_app.py # Standalone face recognition
├── 🖥️ Frontend/                 # GUI components and interface
│   ├── GUI.py                   # Main GUI implementation
│   └── Graphics/                # UI assets and images
├── 🧠 Backend/                  # Core AI and automation
│   ├── Model.py                 # AI decision making
│   ├── Chatbot.py              # Chat interface
│   ├── SpeechToText.py         # Voice recognition
│   ├── TextToSpeech.py         # Voice synthesis
│   ├── RealtimeSearchEngine.py # Web search capabilities
│   ├── Automation.py           # System automation
│   ├── whatsapp.py             # WhatsApp integration
│   ├── call.py                 # Voice/video calling
│   ├── object_detection.py     # Computer vision
│   ├── hand_main.py            # Gesture control
│   ├── auto_updater.py         # Software updates
│   ├── e2e_encryption.py       # Security features
│   ├── simple_*.py             # Modular AI components
│   ├── Data/                   # User data and patterns
│   ├── config/                 # Configuration files
│   └── samples/                # Face recognition samples
├── 📊 logs/                     # System logs and debugging
├── 🔐 secure_keys/              # Protected API keys
├── 🧹 cleanup_scripts/          # Maintenance utilities
├── 🎨 generated_images/         # AI-generated images
├── 💻 generated_code/           # AI-generated code
└── 📞 contacts.db               # Contact database
```

## 🎮 Usage Guide

### 💬 Voice Commands

**Basic Interaction:**
- "Hello Jarvis" - Start conversation
- "Go to sleep" - Put Jarvis in sleep mode
- "Wake up" - Wake Jarvis from sleep mode

**System Commands:**
- "Check system status" - Get system health report
- "Battery status" - Check battery level
- "Show reminders" - Display scheduled reminders
- "Set reminder to [task] at [time]" - Create new reminder

**Communication:**
- "Send message to [contact]" - Send WhatsApp message
- "Call [contact]" - Make voice call
- "Video call [contact]" - Make video call

**Computer Vision:**
- "Start emotion detection" - Begin emotion analysis
- "Turn on hand gesture" - Enable gesture control
- "Object detection" - Start object recognition

**File Operations:**
- "Convert image to PDF" - Image to PDF conversion
- "Open [application]" - Launch applications
- "Close [application]" - Close applications

### 🖱️ Hand Gesture Control

When enabled, control your computer with hand gestures:
- **Cursor Mode**: Move cursor with index finger
- **Click Mode**: Click with thumb and index finger
- **Scroll Mode**: Scroll with hand movements
- **Volume Control**: Adjust system volume
- **Zoom Control**: Zoom in/out in applications

### 🎯 GUI Interface

The modern GUI provides:
- **Home Screen**: System status and quick actions
- **Chat Interface**: Text-based interaction with Jarvis
- **Settings Panel**: Configuration and preferences
- **Real-time Indicators**: System status and activity

**Keyboard Shortcuts:**
- `Ctrl+H`: Home screen
- `Ctrl+C`: Chat screen
- `Ctrl+S`: Settings panel
- `Ctrl+M`: Microphone off
- `Ctrl+U`: Microphone on
- `Escape`: Exit application

## 🔧 Configuration

### 🎙️ Voice Settings
```json
{
  "voice_enabled": true,
  "voice_speed": 1.0,
  "voice_volume": 1.0,
  "language": "en"
}
```

### 🔒 Privacy Settings
```json
{
  "privacy_level": "medium",
  "data_collection": true,
  "secure_mode": false
}
```

### 📡 System Monitoring
```json
{
  "cpu_threshold": 85,
  "memory_threshold": 85,
  "disk_threshold": 90,
  "battery_threshold": 15,
  "monitoring_interval": 60
}
```

## 🧪 Advanced Features

### 🔬 Machine Learning Components
- **Pattern Recognition**: Learns from user behavior patterns
- **Predictive Assistance**: Suggests actions based on context
- **Reinforcement Learning**: Improves responses over time
- **Personalization Engine**: Adapts to user preferences

### 🔐 Security Features
- **End-to-End Encryption**: All communications encrypted
- **Secure Key Management**: Protected API key storage
- **Privacy Modes**: Multiple privacy levels
- **Data Anonymization**: Personal data protection

### 📊 System Integration
- **Real-time Monitoring**: System health and performance
- **Battery Management**: Power monitoring and optimization
- **Application Control**: System-wide automation
- **File Operations**: Advanced file management

## 🐛 Troubleshooting

### 🎥 Camera Issues
- **Error**: "Could not access camera"
- **Solution**: Check camera permissions, close other applications using camera
- **Alternative**: Try different camera indices (0, 1, 2)

### 🎤 Microphone Issues
- **Error**: "Speech recognition failed"
- **Solution**: Check microphone permissions, test audio input
- **Alternative**: Use text-based interaction

### 🔧 Installation Issues
- **Error**: "Module not found"
- **Solution**: Run `python install_dependencies.py` again
- **Alternative**: Install manually with `pip install -r Requirements.txt`

### 🚫 Performance Issues
- **Issue**: Slow response times
- **Solution**: Close unnecessary applications, check system resources
- **Alternative**: Disable computer vision features temporarily

## 🔄 Updates and Maintenance

### 📦 Automatic Updates
Jarvis includes an auto-updater that:
- Checks for new versions automatically
- Downloads and installs updates
- Maintains user data and settings

### 🧹 Maintenance Tasks
- **Log Management**: Automatic log rotation and cleanup
- **Data Cleanup**: Removes temporary files and cache
- **Model Updates**: Updates AI models and recognition data
- **Database Optimization**: Maintains contact and user databases

## 📈 Performance Optimization

### 🚀 Speed Improvements
- **Parallel Processing**: Multiple threads for different tasks
- **Smart Caching**: Cache frequently used data
- **Efficient Models**: Optimized AI models for faster processing
- **Resource Management**: Dynamic resource allocation

### 💾 Memory Management
- **Automatic Cleanup**: Cleans up unused resources
- **Smart Loading**: Loads modules only when needed
- **Cache Limits**: Prevents memory overflow
- **Garbage Collection**: Efficient memory cleanup

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. **Fork the Repository**
   ```bash
   git fork https://github.com/yourusername/jarvis-ai-assistant.git
   ```

2. **Create Feature Branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **Make Changes**
   - Follow Python PEP 8 style guidelines
   - Add tests for new features
   - Update documentation

4. **Submit Pull Request**
   ```bash
   git commit -m "Add amazing feature"
   git push origin feature/amazing-feature
   ```

## 📚 API Documentation

### 🔗 Core Functions
- `MainExecution()`: Main processing loop
- `SpeechRecognition()`: Voice input processing
- `TextToSpeech()`: Voice output generation
- `FirstLayerDMM()`: Decision making model

### 🎯 Extension Points
- **Custom Commands**: Add new voice commands
- **AI Models**: Integrate additional AI models
- **Plugins**: Create custom plugins
- **Themes**: Design custom GUI themes

## 🌐 External Dependencies

### 🔧 Required APIs
- **Groq API**: For AI chat completion
- **OpenCV**: For computer vision
- **MediaPipe**: For hand gesture recognition
- **PyQt5**: For GUI interface

### 📦 Python Packages
See `Requirements.txt` for complete list of dependencies.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **OpenCV Community**: For computer vision capabilities
- **Groq**: For AI model access
- **MediaPipe**: For hand gesture recognition
- **Face Recognition Library**: For facial recognition
- **PyQt5**: for GUI framework
- **All Contributors**: Thank you for making this project better!

## 📞 Support

- **GitHub Issues**: [Report bugs and request features](https://github.com/yourusername/jarvis-ai-assistant/issues)
- **Discussions**: [Join the community](https://github.com/yourusername/jarvis-ai-assistant/discussions)
- **Documentation**: [Read the docs](https://github.com/yourusername/jarvis-ai-assistant/wiki)

---

<div align="center">
  <p>Made with ❤️ by the Jarvis AI Team</p>
  <p>⭐ Star us on GitHub if you find this project useful!</p>
</div> 