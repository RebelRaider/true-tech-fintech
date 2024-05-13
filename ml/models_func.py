import re
from typing import Any

from ml.constatnt import (
    SYSTEM_PROMPT_FOR_HISTORIES,
    SYSTEM_PROMPT_FOR_MANAGER,
    BOT_TOKEN,
    LINEBREAK_TOKEN,
)
from ml.utils import get_message_tokens


def toxic_check(text: str, model) -> bool:
    text = re.sub(r"\W+|\d+", " ", text.lower())

    result = model(text)[0]
    if result["label"] == "LABEL_0":
        return True
    else:
        return False


def interact_manager(
    model: Any,
    conversation: str,
    commands: str,
    top_k: int = 30,
    top_p: float = 0.9,
    temperature: float = 0.2,
    repeat_penalty: float = 1.1,
):
    """
    Взаимодействие с моделью на основе LLAMA для генерации ответов на пользовательские запросы.

    Параметры:
    - model_path (str): Путь к предварительно обученной модели LLAMA.
    - user_prompt (str): Пользовательский запрос для генерации ответа.
    - n_ctx (int): Максимальная длина контекста.
    - top_k (int): Количество наиболее вероятных токенов для рассмотрения в генерации.
    - top_p (float): Порог отсечения для выбора токенов в генерации на основе вероятностей.
    - temperature (float): Параметр температуры для разнообразия в генерации.
    - repeat_penalty (float): Штраф за повторение токенов в генерации.

    Возвращает:
    str: Сгенерированный ответ на основе пользовательского запроса.

    Пример использования:
    ```python
    model_path = "path/to/model"
    user_prompt = "Привет, как дела?"
    response = interact(model_path, user_prompt)
    ```

    Подробности:
    - Функция использует модель LLAMA для генерации ответов на пользовательские запросы.
    - Задает параметры генерации, такие как ограничения токенов, температура и штраф за повторения.
    - Генерирует ответ на основе пользовательского запроса и возвращает его в виде строки.
    """
    tokens = []
    system_message = {"role": "system", "content": SYSTEM_PROMPT_FOR_HISTORIES}
    tokens.extend(get_message_tokens(model, **system_message))
    # Получение токенов пользовательского сообщения
    message_tokens = get_message_tokens(
        model=model,
        role="user",
        content=SYSTEM_PROMPT_FOR_MANAGER.format(commands, conversation),
    )
    token_str = ""
    role_tokens = [model.token_bos(), BOT_TOKEN, LINEBREAK_TOKEN]
    tokens += message_tokens + role_tokens

    # Генерация ответа на основе токенов
    generator = model.generate(
        tokens,
        top_k=top_k,
        top_p=top_p,
        temp=temperature,
        repeat_penalty=repeat_penalty,
    )

    # Преобразование токенов в строку
    for token in generator:
        token_str += model.detokenize([token]).decode("utf-8", errors="ignore")
        tokens.append(token)

        if token == model.token_eos():
            break

    return token_str
