# video_processor.py
import os
import moviepy as mp

def extract_audio_from_video(input_video, output_audio):
    """
    Extract audio from a video file.

    Parameters:
    - input_video: Path to the input video file.
    - output_audio: Path to save the extracted audio.
    """
    if os.path.exists(output_audio):
        print(f"Audio already extracted: {output_audio}")
        return
    
    try:
        print(f"Opening video file: {input_video}")
        video = mp.VideoFileClip(input_video)
        print("Extracting audio...")
        audio = video.audio
        # Specify codec and handle duration
        audio.write_audiofile(output_audio)
        print(f"Audio saved to: {output_audio}")
    except Exception as e:
        print(f"Error extracting audio: {e}")
    finally:
        if 'audio' in locals():
            audio.close()
        if 'video' in locals():
            video.close()