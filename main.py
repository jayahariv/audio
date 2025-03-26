# main.py
import os
import threading
import argparse
from processors.artpark_vaani_hindi import ArtParkVaaniHindiTranscriber
from audio_processor import preprocess_audio
from processors.google_transcriber import GoogleSpeechTranscriber
from processors.oriserve_whisper_hindi import OriserveWhisperHindiTranscriber
from video_processor import extract_audio_from_video

def main(input_file, service, output, skip_preprocessing=False):
    """
    Main function to handle audio/video processing.

    Parameters:
    - file_path: The path to the audio or video file.
    - service: The transcription service to use.
    - skip_preprocessing: Boolean flag to skip preprocessing.
    """
    output_dir = os.path.splitext(input_file)[0]
    
    if not skip_preprocessing:
        # convert the video/audio files to 30secs, of 16K sample rate clips!
        if input_file.lower().endswith(('.mp4', '.avi', '.mov')):
            audio_file = os.path.join(output_dir, "extracted_audio.wav")
            extraction_thread = threading.Thread(target=extract_audio_from_video, args=(input_file, audio_file,))
            extraction_thread.start()
            extraction_thread.join()
        else:
            audio_file = input_file
        
        # Preprocess the audio
        preprocess_audio(audio_file, output_dir)

    if service == "google":
        results = GoogleSpeechTranscriber().transcribeAll(output_dir)
        with open(output, 'w') as f:
            f.write(results)
    elif service == "artpark":
        results = ArtParkVaaniHindiTranscriber().transcribeAll(output_dir)
        with open(output, 'w') as f:
            f.write(results)
    elif service == "oriserv":
        results = OriserveWhisperHindiTranscriber().transcribeAll(output_dir)
        with open(output, 'w') as f:
            f.write(results)
    else:
        print(f"Unknown transcription service: {service}")


    print("Transcription completed and saved to transcription.txt.")

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Process an audio or video file.")
    parser.add_argument("-f", "--file", 
                        required=True, help="Path to the audio or video file")
    parser.add_argument("-s", "--service", choices=["google", "artpark", "oriserv"], 
                        required=True, help="Transcription service to use")
    parser.add_argument("-o", "--output", 
                        required=True, help="Path to the transcription results")
    parser.add_argument("--skip-pre", 
                        action="store_true", 
                        help="Skip preprocessing step")

    args = parser.parse_args()

    main(args.file, args.service, args.output, skip_preprocessing=args.skip_pre)
