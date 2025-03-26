# transcriber.py
import os
import speech_recognition as sr
import subprocess

def transcribe_all_audio(output_dir):
    """
    Transcribe all audio files in the specified directory and save the combined transcription.

    Parameters:
    - output_dir: Directory containing the audio files to transcribe.
    """
    transcription_results = []

    valid_filenames = [
        filename for filename in os.listdir(output_dir)
        if filename.startswith("bas") and filename.endswith(".wav")
    ]

    # Sort the valid filenames by their numeric suffix
    valid_filenames.sort(key=lambda x: int(x[3:-4]))  # Extract the number between 'bas' and '.wav'

    # Loop over files in the output directory
    for filename in valid_filenames:
        audio_file_path = os.path.join(output_dir, filename)
            
        # Transcribe audio
        transcription = transcribe_audio(audio_file_path)
        transcription_results.append(transcription)  # Collect the transcription    
    
    return " ".join(transcription_results)

def transcribe_audio(file_path):
    """
    Transcribe audio to text using Google Speech Recognition.

    Parameters:
    - file_path: Path to the audio file to transcribe.

    Returns:
    - Transcribed text.
    """
    try:
        wav_file_path = os.path.splitext(file_path)[0] + '_converted.wav'
        # Convert to WAV format
        try:
            subprocess.run(['ffmpeg', '-i', file_path, '-acodec', 'pcm_s16le', '-ar', '16000', wav_file_path], check=True)
        except subprocess.CalledProcessError as e:
            return f"Error converting file: {e}"
        recognizer = sr.Recognizer()
        with sr.AudioFile(wav_file_path) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
    
        return text
    except Exception as e:
        return f"Error processing {file_path}: {e}"
    finally:
        # Clean up the converted file if it was created
        if wav_file_path != file_path and os.path.exists(wav_file_path):
            os.remove(wav_file_path)
