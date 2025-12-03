import speech_recognition as sr
import os
from pydub import AudioSegment

def recognize_and_save():
    audio_path = input("Введите полный путь к MP3-файлу: ")
    
    output_dir = "C:/speech_text"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_filename = os.path.join(output_dir, "recognized_text.txt")
    
    try:
        audio = AudioSegment.from_mp3(audio_path)
        wav_path = "temp_audio.wav"
        audio.export(wav_path, format="wav")
    except Exception as e:
        print(f"Ошибка при обработке файла: проверьте путь и наличие FFmpeg. {e}")
        return

    r = sr.Recognizer()

    try:
        with sr.AudioFile(wav_path) as source:
            audio_data = r.record(source)
    except Exception as e:
        print(f"Ошибка при загрузке аудиоданных: {e}")
        os.remove(wav_path)
        return

    os.remove(wav_path)

    recognized_text = ""
    try:
        recognized_text = r.recognize_google(audio_data, language="ru-RU")
        print(f"Распознанный текст:\n{recognized_text}")
    except sr.UnknownValueError:
        print("Речь не распознана.")
    except sr.RequestError as e:
        print(f"Ошибка соединения с API Google: {e}")
    
    try:
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(recognized_text)
        print(f"Результат сохранен в: {output_filename}")
    except Exception as e:
        print(f"Ошибка сохранения файла: {e}")

recognize_and_save()
