
import os
import shutil
import whisper

_model = None


def get_whisper_model():
    global _model

    if _model is None:
        model_name = os.getenv("WHISPER_MODEL", "tiny.en")

        print(f"SPEECH: Loading Whisper model: {model_name}", flush=True)

        _model = whisper.load_model(
            model_name,
            device="cpu"
        )

        print("SPEECH: Whisper model loaded successfully", flush=True)

    return _model


def transcribe_audio(audio_path: str) -> str:
    print("SPEECH: Checking FFmpeg", flush=True)

    if shutil.which("ffmpeg") is None:
        raise RuntimeError("FFmpeg executable not found in system PATH")

    print("SPEECH: Loading Whisper model", flush=True)

    model = get_whisper_model()

    print("SPEECH: Starting transcription", flush=True)

    result = model.transcribe(
        audio_path,
        fp16=False,
        beam_size=1,
        best_of=1,
        verbose=False
    )

    print("SPEECH: Transcription completed", flush=True)

    return result["text"].strip()
