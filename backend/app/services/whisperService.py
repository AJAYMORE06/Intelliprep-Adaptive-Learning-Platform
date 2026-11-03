import os
import shutil

import whisper

_model = None


def get_whisper_model():
    global _model

    if _model is None:
        _model = whisper.load_model("base")

    return _model


def transcribe_audio(audio_path: str) -> str:
    if shutil.which("ffmpeg") is None:
        raise RuntimeError("FFmpeg executable not found in system PATH")

    model = get_whisper_model()
    result = model.transcribe(audio_path, fp16=False)

    return result["text"].strip()
