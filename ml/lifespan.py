from llama_cpp import Llama
import whisper
from loguru import logger
from transformers import pipeline
from ml.constatnt import MODEL_PATH

logger.debug("Init the LLM model")
llm_model = Llama(
    model_path=MODEL_PATH,
    n_gpu_layers=-1,
    n_batch=512,
    n_ctx=4096,
    n_parts=1,
)

logger.debug("Init the whisper model")
whisper_model = whisper.load_model("medium")

logger.debug("Init the toxic classifier model")
toxic_classifier_model = pipeline(
    "text-classification", model="textdetox/xlmr-large-toxicity-classifier"
)
