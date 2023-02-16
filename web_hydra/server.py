#!/usr/bin/env python

from typing import Union

from fastapi import FastAPI
from starlette.responses import FileResponse 

app = FastAPI()

front_folder = "./front/dist"


@app.get("/")
async def index():
    return FileResponse(os.path.join(front_folder, "index.html"))

@app.get("/{protocol}/{url}")
def bruteforce(protocol: str, url: str, q: Union[str, None] = None):
    return {"protocol": protocol, "url": url, "q": q}

