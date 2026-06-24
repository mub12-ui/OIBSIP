# 🎙️ Voice Assistant

A Python-based voice assistant that enables users to interact with their computer using voice commands. The assistant listens to speech, converts it into text, processes commands, and responds through speech.

This project evolved from a beginner-level voice assistant into an advanced smart assistant featuring natural language processing, reminders, weather updates, email functionality, general knowledge answering, custom commands, and simulated smart home control.

---

# 📌 Features

## Beginner Features

✅ Responds to greetings

✅ Tells the current time

✅ Tells the current date

✅ Searches the web based on user queries

✅ Converts speech to text

✅ Converts text to speech

✅ Handles invalid or unrecognized commands

---

## Advanced Features

✅ Weather updates using WeatherAPI

✅ Email sending using SMTP

✅ Reminder system with persistent storage

✅ General knowledge question answering using Wikipedia

✅ Simulated smart home controls

✅ Custom user commands

✅ Basic natural language processing with NLTK

✅ Third-party API integration

✅ Modular architecture

✅ Error handling and security practices

---

# 🛠 Technologies Used

## Programming Language

* Python 3.12

## Libraries

* SpeechRecognition
* PyAudio
* pyttsx3
* requests
* wikipedia
* nltk

## Built-in Modules

* datetime
* webbrowser
* json
* smtplib

---

# 📁 Project Structure

```
voice-assistant/

├── assistant/
│   ├── actions.py
│   ├── command_processor.py
│   ├── speech_recognition.py
│   └── text_to_speech.py
│
├── advanced/
│   ├── api_manager.py
│   ├── custom_commands.py
│   ├── email_service.py
│   ├── knowledge_service.py
│   ├── nlp_processor.py
│   ├── reminder_service.py
│   ├── smart_home.py
│   └── weather_service.py
│
├── config/
│   ├── secrets_example.py
│   └── settings.py
│
├── data/
│   ├── commands.json
│   └── reminders.json
│
├── assets/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/mub12-ui/smart-voice-assistant.git

cd smart-voice-assistant
```

## Create Virtual Environment

```bash
python -m venv .venv
```

## Activate Environment

### Git Bash

```bash
source .venv/Scripts/activate
```

### PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Application

```bash
python main.py
```

---

# 🎤 Example Commands

## Greeting

```
Hello
```

## Time

```
What time is it?
```

## Date

```
What is today's date?
```

## Web Search

```
Search Python tutorials
```

## Weather

```
Weather in Lahore
```

## General Knowledge

```
What is Python programming?
```

```
Who is Alan Turing?
```

## Reminders

```
Remind me study Python
```

```
Show reminders
```

## Smart Home

```
Turn on lights
```

```
Turn off fan
```

## Email

```
Send email
```

## Exit

```
Exit
```

---

# 🔄 Workflow

```
User Speaks
      ↓
Speech Recognition
      ↓
NLP Processing
      ↓
Command Processing
      ↓
Task Execution
      ↓
Text-to-Speech Response
```

---

# 📚 Concepts Covered

* Speech Recognition
* Text-to-Speech
* Natural Language Processing
* Task Automation
* Third-party API Integration
* Email Automation
* Weather APIs
* JSON Data Storage
* Smart Home Simulation
* Error Handling
* Privacy and Security
* Modular Project Architecture

---

# 🔒 Privacy and Security

Sensitive information such as email credentials and API keys are stored in:

```
config/secrets.py
```

This file is excluded from Git using:

```
.gitignore
```

Use:

```
config/secrets_example.py
```

as a template.

---

# 🎯 Learning Outcomes

By completing this project, you will learn:

* Speech recognition systems
* Text-to-speech synthesis
* Natural language processing basics
* API integration
* Email automation
* Persistent data storage with JSON
* Modular Python project organization
* Error handling techniques
* Security best practices

---

# 🚀 Future Improvements

* Better NLP using spaCy
* Wake word detection
* News API integration
* Google Calendar reminders
* GUI using Tkinter or PyQt
* Home Assistant integration
* Conversation history
* AI-powered responses using Gemini or OpenAI APIs

---

# 👨‍💻 Author

**Mubashar Usman**

GitHub: https://github.com/mub12-ui

---

# 📄 License

This project is open source and available under the MIT License.
