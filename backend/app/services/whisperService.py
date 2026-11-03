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
    print("SPEECH: Checking FFmpeg", flush=True)

    if shutil.which("ffmpeg") is None:
        raise RuntimeError("FFmpeg executable not found in system PATH")

    print("SPEECH: Loading Whisper model", flush=True)
    model = get_whisper_model()

    print("SPEECH: Whisper model loaded; starting transcription", flush=True)
    result = model.transcribe(audio_path, fp16=False)

    print("SPEECH: Transcription completed", flush=True)
    return result["text"].strip()
