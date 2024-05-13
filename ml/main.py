from typing import Tuple

from ml.models_func import toxic_check, interact_manager
from ml.utils import get_audio, recognize_audio


def speech2txtPipeline(
    model_whisper, llm_model, toxic_classifier_model, file, commands
) -> Tuple:
    audio, _ = get_audio(model_whisper, file)
    recognized_text = recognize_audio(model_whisper, audio)
    if toxic_check(recognized_text, toxic_classifier_model):
        result_command = interact_manager(llm_model, recognized_text, commands)
    return recognized_text, result_command
