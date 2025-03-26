from base_transcriber import BaseTranscriber
import speech_recognition as sr

class GoogleSpeechTranscriber(BaseTranscriber):
    def transcribe(self, file_path):
        recognizer = sr.Recognizer()
        try:
            with sr.AudioFile(file_path) as source:
                audio_data = recognizer.record(source)
                text = recognizer.recognize_google(audio_data)
                return text
        except sr.UnknownValueError:
            return f"Could not understand audio from: {file_path}"
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"
        except Exception as e:
            return f"Error processing {file_path}: {e}"
