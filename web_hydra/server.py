#!/usr/bin/env python

import os
from typing import Union

from fastapi import FastAPI
from starlette.responses import FileResponse 
from fastapi.staticfiles import StaticFiles

front_folder = "./front/dist"
assets_folder = "./front/dist/assets"

app = FastAPI()
app.mount("/assets", StaticFiles(directory=assets_folder), name="assets")


@app.get("/")
async def index():
    return FileResponse(os.path.join(front_folder, "index.html"))

@app.get("/{protocol}/{url}")
def bruteforce(protocol: str, url: str, q: Union[str, None] = None):
    return {"protocol": protocol, "url": url, "q": q}

