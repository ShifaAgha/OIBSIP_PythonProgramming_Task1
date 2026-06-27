# Voice Assistant (Beginner) — OIBSIP Python Programming, Task 1

A simple Python voice assistant that listens for spoken commands and
responds with speech and text. If no microphone is detected, it
automatically falls back to a typed-text mode so it still runs on any
machine.

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

Add your name, LinkedIn, and GitHub profile link here before submission.

## OIBSIP Submission Notes

- Rename this folder/repo entry to match the required format: `YourName_Task1`
- Push to your `OIBSIP` GitHub repository
- Record a short demo video explaining the code and showing it run, post on LinkedIn
- Submit the GitHub link via the official submission form along with this README
