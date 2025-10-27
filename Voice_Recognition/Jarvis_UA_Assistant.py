import speech_recognition as sr
from gtts import gTTS
import requests, os, json, random
from datetime import datetime
from dotenv import load_dotenv
from langdetect import detect
from textblob import TextBlob
from pydub import AudioSegment
from pydub.playback import play

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OPENWEATHER_KEY = os.getenv("OPENWEATHER_API_KEY")

VOICE_SPEED = False
VOICE_LANG = "uk"
CONVERSATION_HISTORY = []
CONVERSATION_LIMIT = 10
LOG_FILE = "jarvis_log.json"

COMMANDS = {
    "яка година": lambda: f"Зараз {datetime.now().strftime('%H:%M')}",
    "яка дата": lambda: f"Сьогодні {datetime.now().strftime('%d.%m.%Y')}",
}

ANEKDOTY = [
    "Програміст заходить у бар — і каже: «Пиво і пиво».",
    "Якщо щось не працює — спробуй вимкнути й увімкнути!"
]

PORADI = [
    "Посміхайся частіше — це допомагає мозку мислити позитивно.",
    "Не відкладай на завтра те, що можна зробити сьогодні."
]

if __name__ == "__main__":
    main_loop()