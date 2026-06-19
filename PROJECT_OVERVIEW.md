# Supru AI Assistant – Project Overview

## Developer

Sanjeev Santhosh

## Project Name

Supru – Personal AI Voice Assistant

## Vision

Supru is a personal AI assistant being developed from scratch using Python. The long-term goal is to create an intelligent voice-controlled AI agent capable of understanding voice commands, interacting with the computer, remembering information, controlling applications, filling forms, browsing the web, and assisting with daily tasks.

The inspiration comes from assistants such as ChatGPT, Gemini, Siri, Alexa, and Google Assistant, but Supru is intended to be fully personalized and customizable.

---

# Development Journey

## Stage 1 – Project Setup

Created the project folder structure.

Installed Python dependencies:

* SpeechRecognition
* PyAudio
* Edge-TTS
* Pygame

Created a virtual environment for project isolation.

---

# Stage 2 – Voice Output

Initially used:

* pyttsx3

Goal:

Convert text into speech.

### Problem Encountered

The assistant would speak only the first sentence.

Example:

"Hello Sanjeev"

worked correctly, but subsequent speech outputs became silent.

Terminal output continued normally.

### Investigation

Multiple tests were performed:

1. Reinitializing the speech engine
2. Using engine.stop()
3. Changing voice configurations
4. Testing multiple runAndWait() calls
5. Running standalone speech scripts

### Result

Discovered a compatibility issue between:

* Python 3.13
* Windows 11
* pyttsx3

The library could only produce the first speech output reliably.

### Solution

Migrated from pyttsx3 to:

* Edge-TTS
* Pygame

Benefits:

* Better voice quality
* More natural speech
* Reliable repeated responses

---

# Stage 3 – Speech Recognition

Implemented microphone input using:

* SpeechRecognition
* Google Speech Recognition API

Capabilities achieved:

* Listen through microphone
* Convert speech into text
* Display recognized text in terminal

Example:

User:

Hello Supru

Recognized:

hello supru

---

# Stage 4 – Continuous Listening System

Originally Supru listened once and exited.

Implemented:

while True:

continuous listening loop.

Result:

Supru remains active until explicitly instructed to stop.

---

# Stage 5 – Command Processing

Implemented basic commands.

Current Commands:

### Greeting

User:

Hello

Response:

Hello Sanjeev

---

### Time

User:

What is the time?

Response:

Current system time

---

### Date

User:

What is today's date?

Response:

Current system date

---

### How are you

User:

How are you?

Response:

I am doing great. Thank you for asking.

---

### Unknown Commands

User:

Anything else

Response:

I heard [command]

---

### Exit

User:

Exit

or

Goodbye

Response:

Goodbye Sanjeev

Program terminates safely.

---

# Current Architecture

User Voice
↓
Microphone
↓
Speech Recognition
↓
Command Processing
↓
Response Generation
↓
Edge-TTS
↓
Speaker Output

---

# Current Status

Version:

Supru v1.0

Completed Features:

✓ Voice Recognition

✓ Natural Voice Output

✓ Continuous Listening

✓ Time Query

✓ Date Query

✓ Greeting Responses

✓ Exit Command

✓ Real-Time Voice Conversation

---

# Future Development Roadmap

## Phase 2 – Desktop Control

Planned Features:

Open Chrome

Open VS Code

Open Notepad

Open Calculator

Open File Explorer

Shutdown Computer

Restart Computer

Launch Applications Using Voice Commands

---

## Phase 3 – Browser Automation

Planned Features:

Open YouTube

Search Google

Search YouTube

Open Websites

Navigate Browser Tabs

Perform Automated Web Tasks

---

## Phase 4 – Personal Memory System

Planned Features:

Remember Name

Remember Address

Remember Phone Number

Remember College Information

Remember User Preferences

Example:

"Remember my address"

Store permanently.

Later:

"What is my address?"

Supru retrieves stored information.

---

## Phase 5 – AI Intelligence Layer

Planned Features:

General Conversation

Question Answering

Learning User Preferences

Task Planning

Personal Assistance

Integration with Large Language Models

Examples:

ChatGPT API

Local AI Models

Ollama

Llama

Mistral

---

## Phase 6 – Screen Understanding

Planned Features:

Read Screen Content

Take Screenshots

Detect Errors

Read Documents

Analyze User Interface Elements

Provide Context-Aware Assistance

---

## Phase 7 – Form Filling Assistant

Planned Features:

Automatic Form Filling

Application Assistance

License Forms

Government Forms

College Forms

Job Applications

Use stored personal information to complete forms automatically.

---

## Phase 8 – Autonomous AI Agent

Long-Term Vision

User:

"Hey Supru"

Supru activates.

User:

"Apply for my license"

Supru:

Opens browser

Navigates website

Fills forms

Uploads documents

Reviews information

Requests confirmation

Submits application

---

# Ultimate Goal

To develop a fully functional personal AI assistant capable of:

* Voice Interaction
* Computer Control
* Memory
* Web Automation
* Form Filling
* Personal Assistance
* AI-Powered Decision Support

Supru is being developed as both a learning project and a practical AI assistant system, with the objective of becoming a complete AI agent comparable to modern intelligent assistants.
