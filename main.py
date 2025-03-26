# main.py
import os
import sys
from audio_processor import preprocess_audio, boost_audio
from video_processor import extract_audio_from_video
from transcriber import transcribe_all_audio

def main(input_file):
    output_dir = os.path.splitext(input_file)[0]  # Create a folder named after the input file

    # ----- 
    # This code will convert the video/audio files to 30secs, of 16K sample rate clips!
    # -- 
    # Check if the input is a video or an audio file
    if input_file.lower().endswith(('.mp4', '.avi', '.mov')):
        audio_file = os.path.join(output_dir, "extracted_audio.wav")
        extract_audio_from_video(input_file, audio_file)
    else:
        audio_file = input_file
    
    # Preprocess the audio
    preprocess_audio(audio_file, output_dir)
    if os.path.exists(audio_file):
        os.remove(audio_file)

    # ----- 

    # Transcribe audio
    transcription = transcribe_all_audio(output_dir)
    
    # Save transcription to text file
    with open(os.path.join(output_dir, "transcription.txt"), 'w') as f:
        f.write(transcription)

    print("Transcription completed and saved to transcription.txt.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_audio_or_video>")
        sys.exit(1)
    main(sys.argv[1])
