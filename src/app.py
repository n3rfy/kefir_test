from fastapi import FastAPI, Request
from .api import router
from fastapi.responses import JSONResponse
from .core.exc_class import ExceptionAll

app = FastAPI()

@app.exception_handler(ExceptionAll)
def validation_exception_handler(request: Request, exc: ExceptionAll):
    return JSONResponse(
        status_code=exc.status_code, 
        content=exc.content
    )

app.include_router(router)
