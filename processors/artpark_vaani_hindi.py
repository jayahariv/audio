import torch

from transformers import pipeline
from base_transcriber import BaseTranscriber

class ArtParkVaaniHindiTranscriber(BaseTranscriber):
    def transcribe(self, file_path):
        modelTags="ARTPARK-IISc/whisper-small-vaani-hindi"
        transcribe = pipeline(task="automatic-speech-recognition", model=modelTags, chunk_length_s=30, device="cpu")
        transcribe.model.config.forced_decoder_ids = transcribe.tokenizer.get_decoder_prompt_ids(language="hi", task="transcribe")
        return transcribe(file_path)["text"]
