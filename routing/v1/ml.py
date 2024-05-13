from typing import List
from fastapi import APIRouter, Depends
from schemas.ml import MlRequest, MlResponse
from ml.main import speech2txtPipeline
from ml.lifespan import whisper_model, toxic_classifier_model, llm_model
from services.active_action import ActiveActionService
import tempfile

router = APIRouter(prefix="/api/v1/ml", tags=["ml"])


@router.post(
    "/do_ml/",
    summary="делает ml",
    response_model=List[MlResponse],
)
async def do_all(
    req: MlRequest,
    active_action_service: ActiveActionService = Depends(),
):
    with tempfile.NamedTemporaryFile() as temp_file:
        temp_file.write(req.voice.file.read())
        file_path = temp_file.name
        next_tasks = await active_action_service.get_next_tasks(req.action_id)
        commands = "\n".join(
            [f"{next_task.name}-{next_task.description}" for next_task in next_tasks]
        )
        text = speech2txtPipeline(
            whisper_model,
            llm_model,
            toxic_classifier_model,
            file_path,
            commands=commands,
        )
        return [MlResponse(command=text)]
