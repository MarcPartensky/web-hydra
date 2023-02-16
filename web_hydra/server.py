#!/usr/bin/env python

import os
import subprocess
from typing import Union

from fastapi import FastAPI, HTTPException
from starlette.responses import FileResponse 
from fastapi.staticfiles import StaticFiles

front_folder = "./front/dist"
assets_folder = "./front/dist/assets"
public_folder = "./front/public"

app = FastAPI()
app.mount("/assets", StaticFiles(directory=assets_folder), name="assets")
app.mount("/public", StaticFiles(directory=public_folder), name="public")


@app.get("/")
async def index():
    return FileResponse(os.path.join(front_folder, "index.html"))

@app.get("/query")
def query(q: Union[str, None] = None):
    return {"q": q}

@app.get("/{protocol}/{url}")
def bruteforce(protocol: str, url: str, q: Union[str, None] = None):
    return {"protocol": protocol, "url": url, "q": q}

@app.get("/shell")
def shell(q: Union[str, None] = None):
    if not q:
        raise HTTPException(status_code=404, detail="Incomplete get params.")
    cmd = q["cmd"]
    words = cmd.split(" ")
    out = subprocess.run(words, capture_output=True)
    return {"output": out.stdout}
