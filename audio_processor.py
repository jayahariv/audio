# audio_processor.py
import os
import numpy as np
import librosa
from scipy.io.wavfile import write

def preprocess_audio(input_file, output_dir, target_sr=16000, duration=30):
    """
    Preprocess the audio file: resample to 16000 Hz and trim/pad to 30 seconds.
    
    Parameters:
    - input_file: Path to the input audio file.
    - output_dir: Directory to save the processed audio.
    - target_sr: Target sample rate (default is 16000).
    - duration: Duration in seconds for the output audio (default is 30).
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Load the audio file
    audio, sr = librosa.load(input_file, sr=None)
    total_duration = len(audio) / sr  # Calculate total duration in seconds
    try:
    
        # Resample to target sample rate
        if sr != target_sr:
            audio = librosa.resample(audio, orig_sr=sr, target_sr=target_sr)
        
        # Loop to create segments
        for start_time in range(0, int(total_duration), duration):
            end_time = min(start_time + duration, total_duration)
            start_sample = int(start_time * target_sr)
            end_sample = int(end_time * target_sr)
            segment = audio[start_sample:end_sample]  # Extract the segment

            # Trim or pad the audio to the required duration
            target_length = target_sr * duration
            if len(segment) > target_length:
                segment = segment[:target_length]  # Trim
            else:
                segment = np.pad(segment, (0, max(0, target_length - len(segment))), mode='constant')  # Pad

            # Save the processed wav audio! For debugging use this! 
            # output_file = os.path.join(output_dir, f"audio_segment_{start_time // duration + 1}.wav")
            # write(output_file, target_sr, segment.astype(np.float32))  # Save as WAV file
            # print(f"Extracted and processed: {output_file}")
            
            boosted_audio_file = os.path.join(output_dir, f"bas{start_time // duration + 1}.wav")
            boost_audio(segment, boosted_audio_file)  # Boost and save
            print(f"Boosted audio saved: {boosted_audio_file}")
        
        return output_dir
    except Exception as e:
        print(f"Error extracting audio: {e}")
    finally:
        print("finished")

def boost_audio(audio_data, output_file):
    """
    Boost the audio data and save it to the specified output file.

    Parameters:
    - audio_data: NumPy array containing the audio data to boost.
    - output_file: Path to save the boosted audio file.
    """
    # Example boost: increase the volume by a factor (e.g., 2.0)
    boosted_audio = audio_data * 2.0  # Adjust the boost factor as necessary
    boosted_audio = np.clip(boosted_audio, -1.0, 1.0)  # Clip to prevent distortion

    # Save the boosted audio as a WAV file
    write(output_file, 16000, boosted_audio.astype(np.float32))  # Save with target sample rate
