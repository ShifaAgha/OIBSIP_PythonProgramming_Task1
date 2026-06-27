"""
Voice Assistant (Beginner Level) - OIBSIP Python Programming Task 1
---------------------------------------------------------------------
Features:
    1. Responds to greetings ("hello", "hi", "hey") with a predefined reply.
    2. Tells the current time and date.
    3. Searches the web (Google) or Wikipedia for a topic spoken by the user.
    4. Falls back to a typed-text mode automatically if no microphone is
       detected, so the assistant still works on machines without audio
       hardware (or for quick testing).
    5. Includes basic error handling for speech-recognition failures,
       network issues, and unrecognized commands.

Run:
    python voice_assistant.py
"""

import datetime
import sys
import webbrowser

try:
    import speech_recognition as sr
except ImportError:
    sr = None

try:
    import pyttsx3
except ImportError:
    pyttsx3 = None

try:
    import wikipedia
except ImportError:
    wikipedia = None


# ---------------------------------------------------------------------------
# Text-to-speech setup
# ---------------------------------------------------------------------------
engine = None
if pyttsx3:
    try:
        engine = pyttsx3.init()
        engine.setProperty("rate", 170)
    except Exception:
        engine = None


def speak(text):
    """Speak the given text out loud (if TTS is available) and print it."""
    print(f"Assistant: {text}")
    if engine:
        try:
            engine.say(text)
            engine.runAndWait()
        except Exception:
            pass


# ---------------------------------------------------------------------------
# Listening (voice or text fallback)
# ---------------------------------------------------------------------------
def mic_available():
    """Check whether speech_recognition + a working microphone are present."""
    if sr is None:
        return False
    try:
        with sr.Microphone():
            pass
        return True
    except Exception:
        return False


def listen_voice(recognizer):
    """Capture one voice command and convert it to lowercase text."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source, timeout=6, phrase_time_limit=8)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio, language="en-in")
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Could you repeat it?")
    except sr.RequestError:
        speak("I can't reach the speech recognition service right now. "
              "Please check your internet connection.")
    except sr.WaitTimeoutError:
        speak("I didn't hear anything.")
    return ""


def listen_text():
    """Fallback: read a command typed by the user."""
    try:
        return input("You (type command): ").lower()
    except (EOFError, KeyboardInterrupt):
        return "exit"


# ---------------------------------------------------------------------------
# Skill / command handlers
# ---------------------------------------------------------------------------
GREETINGS = ("hello", "hi", "hey", "good morning", "good afternoon", "good evening")
EXIT_WORDS = ("exit", "quit", "stop", "bye", "goodbye")


def handle_greeting():
    hour = datetime.datetime.now().hour
    if hour < 12:
        part_of_day = "morning"
    elif hour < 17:
        part_of_day = "afternoon"
    else:
        part_of_day = "evening"
    speak(f"Hello! Good {part_of_day}. How can I help you today?")


def handle_time():
    now = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {now}.")


def handle_date():
    today = datetime.datetime.now().strftime("%A, %d %B %Y")
    speak(f"Today's date is {today}.")


def handle_wikipedia(command):
    if wikipedia is None:
        speak("The wikipedia module isn't installed, so I can't search "
              "Wikipedia right now.")
        return
    topic = command.replace("wikipedia", "").replace("search", "").strip()
    if not topic:
        speak("What would you like me to look up on Wikipedia?")
        return
    speak(f"Searching Wikipedia for {topic}...")
    try:
        summary = wikipedia.summary(topic, sentences=2)
        speak(summary)
    except wikipedia.exceptions.DisambiguationError:
        speak("That topic is ambiguous. Could you be more specific?")
    except wikipedia.exceptions.PageError:
        speak("I couldn't find anything on Wikipedia for that topic.")
    except Exception:
        speak("Something went wrong while searching Wikipedia. "
              "Please check your internet connection.")


def handle_google_search(command):
    query = command.replace("search", "").replace("google", "").replace("for", "", 1).strip()
    if not query:
        speak("What would you like me to search for?")
        return
    speak(f"Here are the search results for {query}.")
    try:
        webbrowser.open(f"https://www.google.com/search?q={query}")
    except Exception:
        speak("I couldn't open a browser window to show the results.")


def handle_open_site(command):
    sites = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "github": "https://www.github.com",
        "wikipedia": "https://www.wikipedia.org",
    }
    for name, url in sites.items():
        if name in command:
            speak(f"Opening {name}.")
            webbrowser.open(url)
            return True
    return False


def handle_unknown():
    speak("I'm not sure how to help with that yet. Try asking me for the "
          "time, the date, to search something, or just say hello.")


# ---------------------------------------------------------------------------
# Command router
# ---------------------------------------------------------------------------
def process_command(command):
    """Return False to stop the assistant, True to keep running."""
    if not command:
        return True

    if any(word in command for word in EXIT_WORDS):
        speak("Goodbye! Have a great day.")
        return False

    if any(greeting in command for greeting in GREETINGS):
        handle_greeting()
    elif "time" in command:
        handle_time()
    elif "date" in command or "day" in command:
        handle_date()
    elif "wikipedia" in command:
        handle_wikipedia(command)
    elif handle_open_site(command):
        pass
    elif "search" in command or "google" in command:
        handle_google_search(command)
    else:
        handle_unknown()

    return True


# ---------------------------------------------------------------------------
# Main loop
# ---------------------------------------------------------------------------
def main():
    print("=" * 60)
    print(" Voice Assistant - OIBSIP Python Programming Task 1")
    print("=" * 60)

    use_voice = mic_available()
    recognizer = sr.Recognizer() if (use_voice and sr) else None

    if use_voice:
        speak("Voice mode enabled. I'm listening for your commands.")
    else:
        speak("No microphone detected, switching to text mode. "
              "Type your commands below.")

    speak("You can say things like: hello, what's the time, what's the "
          "date, search wikipedia for python, search google for news, "
          "or open youtube. Say exit to quit.")

    running = True
    while running:
        try:
            if use_voice:
                command = listen_voice(recognizer)
            else:
                command = listen_text()
        except KeyboardInterrupt:
            print()
            speak("Goodbye!")
            break

        running = process_command(command)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"Unexpected error: {exc}", file=sys.stderr)
        sys.exit(1)
