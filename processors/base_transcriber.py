import os

class BaseTranscriber:
    def transcribe(self, file_path):
        raise NotImplementedError("Subclasses should implement this method.")
    
    # we will only consider bas<decimal>.wav files.
    def transcribeAll(self, output_dir):
        valid_filenames = [
            filename for filename in os.listdir(output_dir)
            if filename.startswith("final_audio") and filename.endswith(".wav")
        ]

        # Sort the valid filenames by their numeric suffix
        # remove the 'final_word' and '.wav' to form the number alone! 
        valid_filenames.sort(key=lambda x: int(x[11:-4]))
        results = []
        
        for file_path in valid_filenames:
            audio_file_path = os.path.join(output_dir, file_path)
            t = self.preprocess(audio_file_path, self.transcribe)
            results.append(t)
        return " ".join(results)
    
    def preprocess(self, file_path, callback):
        try:
            
            # if there is any additional common preprocess required, we can do here! 
            
            res = callback(file_path)

            return res 
        
        except Exception as e:
            return f"Error processing {file_path}: {e}"
    
    
