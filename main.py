import os

import jsonify
from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel

from google_search import get_search_results
from html_parser import parse_html_content
from json_formatter import format_search_results

app = FastAPI()

class InputData(BaseModel):
    query: str
    query2: str


@app.post("/post_endpoint/")
async def post_endpoint(data: InputData):
    query = data.query
    if not query:
        return jsonify({'error': 'Missing query parameter'}), 400

    # Retrieve search results
    results = get_search_results(query)

    # Parse HTML content and extract relevant information
    parsed_results = []
    for result in results:
        parsed_result = parse_html_content(result["link"], result["snippet"])
        parsed_results.append(parsed_result)

    # Format search results as JSON
    formatted_results = format_search_results(parsed_results)

    return formatted_results


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
    uvicorn.run("main:app", host="0.0.0.0", port=80, reload = True)
