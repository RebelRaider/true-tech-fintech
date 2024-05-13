from typing import List, Dict, Any
import whisper
from ml.constatnt import ROLE_TOKENS, LINEBREAK_TOKEN, SYSTEM_PROMPT_FOR_HISTORIES


def get_message_tokens(model: Any, role: str, content: str) -> List[int]:
    """
    Создает токены для сообщения с учетом роли и содержания.

    Параметры:
    - model (Any): Модель токенизатора.
    - role (str): Роль сообщения.
    - content (str): Содержание сообщения.

    Возвращает:
    List[int]: Список токенов сообщения.

    Пример использования:
    ```python
    model = SomeTokenizer()
    role = "user"
    content = "Hello, world!"
    message_tokens = get_message_tokens(model, role, content)
    ```

    Подробности:
    - Функция токенизирует содержание сообщения с учетом роли и вставляет соответствующие токены.
    - В конце сообщения добавляется токен окончания строки.
    """
    message_tokens = model.tokenize(content.encode("utf-8"))
    message_tokens.insert(1, ROLE_TOKENS[role])
    message_tokens.insert(2, LINEBREAK_TOKEN)
    message_tokens.append(model.token_eos())
    return message_tokens


def convert_to_tokens(messages: List[Dict[str, str]], model: Any) -> List[int]:
    """
    Преобразует список сообщений в токены.

    Параметры:
    - messages (List[Dict[str, str]]): Список сообщений в формате JSON.
    - model (Any): Модель токенизатора.

    Возвращает:
    List[int]: Список токенов всех сообщений.
    """
    tokens = []
    system_message = {"role": "system", "content": SYSTEM_PROMPT_FOR_HISTORIES}
    tokens.extend(get_message_tokens(model, **system_message))
    for message in messages:
        role = message["role"]
        content = message["message"]
        message_tokens = get_message_tokens(model, role, content)
        tokens.extend(message_tokens)
    tokens.extend(get_message_tokens(model, **system_message))
    return tokens


def get_system_tokens(model: Any) -> List[int]:
    """
    Создает токены для системного сообщения.

    Параметры:
    - model (Any): Модель токенизатора.

    Возвращает:
    List[int]: Список токенов системного сообщения.

    Пример использования:
    ```python
    model = SomeTokenizer()
    system_tokens = get_system_tokens(model)
    ```

    Подробности:
    - Функция создает токены для системного сообщения, добавляя соответствующие маркеры.
    """
    system_message = {"role": "system", "content": SYSTEM_PROMPT_FOR_HISTORIES}
    return get_message_tokens(model, **system_message)


def get_audio(model_whisper, file_path: str):
    audio = whisper.load_audio(file_path)
    audio = whisper.pad_or_trim(audio)
    mel = whisper.log_mel_spectrogram(audio).to(model_whisper.device)
    _, probs = model_whisper.detect_language(mel)
    return mel, max(
        probs, key=probs.get
    )  #  max(probs, key=probs.get) -> возвращает язык и его вероятность


def recognize_audio(model_whisper, mel) -> str:
    options = whisper.DecodingOptions()
    result = whisper.decode(model_whisper, mel, options)
    return result.text
