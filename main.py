from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

import calculator

BASE_DIR = Path(__file__).resolve().parent


def find_static_dir() -> Path:
    # Works whether index.html is in static/ or in static/static/
    for candidate in (BASE_DIR / "static", BASE_DIR / "static" / "static"):
        if (candidate / "index.html").exists():
            return candidate
    return BASE_DIR / "static"


STATIC_DIR = find_static_dir()

app = FastAPI(title="Multi-Purpose Calculator")


class CalcIn(BaseModel):
    condition: int
    values: list[float] = []


@app.get("/api/operations")
def operations():
    """The menu: condition number, name and the inputs each option needs."""
    return {
        "operations": [
            {"id": cid, "name": name, "inputs": labels, "exit": func is None}
            for cid, name, labels, func in calculator.OPERATIONS
        ]
    }


@app.post("/api/calculate")
def calculate(data: CalcIn):
    try:
        result = calculator.run(data.condition, data.values)
    except calculator.CalcError as err:
        raise HTTPException(status_code=400, detail=str(err))
    return {"result": result}


# check_dir=False so the server still starts (and shows a clear message)
# even if the static folder was not uploaded
app.mount("/static", StaticFiles(directory=STATIC_DIR, check_dir=False), name="static")


@app.get("/")
def home():
    index = STATIC_DIR / "index.html"
    if index.exists():
        return FileResponse(index)
    return {"error": "index.html not found in the static folder"}
