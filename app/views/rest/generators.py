from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse

from app.tasks import generate_email_addresses

router = APIRouter()


@router.post("/email_address", tags=['generators'], status_code=201)
async def run_task(data=Body(...)):
    count = int(data["count"])
    task = generate_email_addresses.delay(count)
    return JSONResponse({"Result": task.get()})
