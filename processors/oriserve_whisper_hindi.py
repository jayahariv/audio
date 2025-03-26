import torch

from transformers import pipeline
from processors.base_transcriber import BaseTranscriber

class OriserveWhisperHindiTranscriber(BaseTranscriber):
    def transcribe(self, file_path):
        modelTags="Oriserve/Whisper-Hindi2Hinglish-Prime"
        transcribe = pipeline(task="automatic-speech-recognition", model=modelTags, chunk_length_s=30, device="cpu")
        transcribe.model.config.forced_decoder_ids = transcribe.tokenizer.get_decoder_prompt_ids(language="en", task="transcribe")
        return transcribe(file_path)["text"]
