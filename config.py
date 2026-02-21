"""конфиг Нефеша"""

# ?ОСНОВНОЕ
ASSISTANT_NAME = "нефеш"
LANGUAGE = "ru"

# ?ПУТИ
VOSK_MODEL_PATH = "model"

# ?TTS
TTS_RATE = 150        # Скорость речи (слов в минуту)
TTS_VOLUME = 0.9      # Громкость голоса (0.0 - 1.0)

# ?РАСПОЗНОВАНИЕ
LISTEN_TIMEOUT = 5    # Сколько секунд слушать команду
SAMPLE_RATE = 16000   # Частота дискретизации аудио

# ?ПРИЛОЖЕНИЯ
APPS = {
    "блокнот": "notepad.exe",
    "калькулятор": "calc.exe",
    "проводник": "explorer.exe",
    "яндекс музыка": "Яндекс Музыка.exe",
    "дискорд": "Discord.exe",
    "телега": "Telegram.exe",
    "телеграм": "Telegram.exe",
}

# ?САЙТЫ
SITES = {
    "ютуб": "https://www.youtube.com",
    "гугл": "https://www.google.com",
    "гитхаб": "https://github.com",
}
