# main.py
import os
import sys
import threading
from processors.artpark_vaani_hindi import ArtParkVaaniHindiTranscriber
from audio_processor import preprocess_audio
from processors.google_transcriber import GoogleSpeechTranscriber
from video_processor import extract_audio_from_video

def main(input_file):
    output_dir = os.path.splitext(input_file)[0]  # Create a folder named after the input file

    # ----- 
    # This code will convert the video/audio files to 30secs, of 16K sample rate clips!
    # -- 
    # Check if the input is a video or an audio file
    if input_file.lower().endswith(('.mp4', '.avi', '.mov')):
        audio_file = os.path.join(output_dir, "extracted_audio.wav")
        extraction_thread = threading.Thread(target=extract_audio_from_video, args=(input_file, audio_file,))
        extraction_thread.start()
        extraction_thread.join()
    else:
        audio_file = input_file
    
    # Preprocess the audio
    preprocess_audio(audio_file, output_dir)

    # GOOGLE Transcribe!
    google_results = GoogleSpeechTranscriber().transcribeAll(output_dir)
    with open(os.path.join(output_dir, "gg_t.txt"), 'w') as f:
        f.write(google_results)

    # ArtPark Vaani Hindi Transcribe!
    artpark_results = ArtParkVaaniHindiTranscriber().transcribeAll(output_dir)
    with open(os.path.join(output_dir, "art_t.txt"), 'w') as f:
        f.write(artpark_results)

    print("Transcription completed and saved to transcription.txt.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_audio_or_video>")
        sys.exit(1)
    main(sys.argv[1])
