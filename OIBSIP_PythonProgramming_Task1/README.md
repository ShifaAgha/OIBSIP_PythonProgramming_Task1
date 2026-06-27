# Voice Assistant (Beginner) — OIBSIP Python Programming, Task 1

This project is a Python-based voice assistant developed for the OIBSIP Python Programming Internship. It can recognize voice commands, provide spoken responses, perform web searches, retrieve information from Wikipedia, and automatically switch to text mode when a microphone is unavailable.

## Overview

The Voice Assistant is a beginner-level Python application designed to demonstrate speech recognition, text-to-speech conversion, and web automation. The assistant can interact through voice commands and continue working through keyboard input if audio hardware is not available.


## Learning Outcomes

Through this project, I gained practical experience with:

- Speech Recognition using Python
- Text-to-Speech conversion
- Browser automation
- Working with external Python libraries
- Error and exception handling
- Building interactive command-line applications

## Features

- Responds to greetings ("hello", "hi", "good morning", etc.)
- Tells the current time
- Tells the current date
- Searches Wikipedia for a topic and reads back a short summary
- Searches Google for a query and opens the results in the browser
- Opens common websites by name (YouTube, GitHub, Wikipedia, Google)
- Falls back to keyboard input automatically when no microphone is found
- Handles speech-recognition errors, network errors, and unknown commands gracefully

## Tech Stack

- Python 3
- [`SpeechRecognition`](https://pypi.org/project/SpeechRecognition/) — converts speech to text via Google's free Web Speech API
- [`pyttsx3`](https://pypi.org/project/pyttsx3/) — offline text-to-speech engine
- [`PyAudio`](https://pypi.org/project/PyAudio/) — microphone input
- [`wikipedia`](https://pypi.org/project/wikipedia/) — Wikipedia summary lookups
- `datetime`, `webbrowser` — built-in standard library modules

## Setup

1. Clone the repository and move into this task's folder.
2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   **Note on PyAudio:** PyAudio can fail to install with plain `pip` on
   some systems because it needs PortAudio.
   - Windows: `pip install pipwin && pipwin install pyaudio`
   - macOS: `brew install portaudio` then `pip install pyaudio`
   - Linux (Debian/Ubuntu): `sudo apt-get install python3-pyaudio` or
     `sudo apt-get install portaudio19-dev` then `pip install pyaudio`

3. Run the assistant:

   ```bash
   python voice_assistant.py
   ```
   
4. If the Wikipedia module is missing, install it using:

   ```bash
   pip install wikipedia
   ```

### Troubleshooting

- **`No module named 'distutils'`** — Python 3.12+ removed the built-in
  `distutils` module, which an older dependency still expects. Fix:
  
  ```bash
  pip install --upgrade setuptools
  ```
  
- **`pyaudio` fails to build / "Microsoft Visual C++ 14.0 required"** — this
  usually happens on very new Python versions (e.g. 3.13/3.14) that don't yet
  have pre-built PyAudio wheels. Easiest fix: install Python 3.12 alongside
  your current version and run this project with `py -3.12` instead.
- **Assistant says "No microphone detected" even though you have one** — open
  Windows Settings → System → Sound → Input, and make sure your actual
  microphone (e.g. "Microphone Array") is set as the **default input
  device**, not an unplugged headset.

If a microphone isn't available (or the required libraries aren't
installed), the assistant prints a notice and switches to text mode —
just type your commands instead of speaking them.

## Example Commands

| Say / Type                          | Result                                  |
|--------------------------------------|------------------------------------------|
| `hello`                               | Greets you back based on time of day     |
| `what is the time`                    | Tells the current time                   |
| `what is the date`                    | Tells the current date                   |
| `search wikipedia for python`         | Reads a short Wikipedia summary          |
| `search google for ai news`           | Opens Google search results in browser   |
| `open youtube`                        | Opens YouTube in browser                 |
| `exit` / `quit` / `bye`               | Ends the program                         |

## Project Structure

```
voice_assistant/
├── voice_assistant.py   # main program
├── requirements.txt     # dependencies
└── README.md            # this file
```

## Possible Future Enhancements

- Add natural language understanding (NLP) for more flexible phrasing
- Add email sending, reminders, and weather updates (Advanced task level)
- Wake-word detection so the assistant only listens after a trigger phrase
- GUI front-end instead of the console

## Author

**Shifa Agha**

GitHub Repository: https://github.com/ShifaAgha/OIBSIP


## Internship Information

- Organization: Oasis Infobyte
- Domain: Python Programming
- Task: Task 1 – Voice Assistant

This project was completed as part of the Oasis Infobyte Internship Program to demonstrate the implementation of a basic voice-controlled assistant using Python.
