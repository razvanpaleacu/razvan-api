from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    string_data: str
    int_data: int
    float_data: float
    bool_data: bool
    list_data: List[int]
    optional_data: Optional[str]

@app.post("/post_endpoint/")
async def post_endpoint(data: InputData):
    return data

@app.get("/get_endpoint/")
async def get_endpoint(string_data: str, int_data: int, float_data: float, bool_data: bool, list_data: List[int] = [], optional_data: Optional[str] = None):
    return {
        "string_data": string_data,
        "int_data": int_data,
        "float_data": float_data,
        "bool_data": bool_data,
        "list_data": list_data,
        "optional_data": optional_data or "None"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)
