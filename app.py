from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel
import uvicorn
import sys
import os
import json
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse, JSONResponse
from fastapi.responses import Response

from src.textSummarizer.pipeline.prediction_pipeline import PredictionPipeline


class PredictionRequest(BaseModel):
    text: str


text: str = "What is Text Summarization?"

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Handle JSON parsing and validation errors"""
    try:
        body = await request.body()
        body_text = body.decode("utf-8")
        # Try to parse the JSON manually
        data = json.loads(body_text)
        return JSONResponse(
            status_code=200,
            content={
                "summary": PredictionPipeline().predict(data.get("text", ""))
            }
        )
    except json.JSONDecodeError as e:
        return JSONResponse(
            status_code=400,
            content={"detail": f"Invalid JSON: {str(e)}"}
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"detail": f"Error processing request: {str(e)}"}
        )


@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")


@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training successful !!")

    except Exception as e:
        return Response(f"Error Occurred! {e}")


@app.post("/predict")
async def predict_route(request: PredictionRequest):
    try:
        obj = PredictionPipeline()
        output = obj.predict(request.text)
        return {"summary": output}
    except Exception as e:
        raise e


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
