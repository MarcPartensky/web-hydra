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
def shell(cmd: Union[str, None] = None):
    if not cmd:
        raise HTTPException(status_code=404, detail="Incomplete get params.")
    words = cmd.split(" ")
    print(words)
    out = subprocess.run(words, capture_output=True)
    return {"output": out.stdout}

@app.get("/hydra")
def hydra(cmd: Union[str, None] = None):
    if not cmd:
        raise HTTPException(status_code=404, detail="Incomplete get params.")
    words = cmd.split(" ")
    print(words)

    out = subprocess.run(["hydra"] + words, capture_output=True)
    return {"output": out.stdout}


def hydra_cmd(protocol: str, interface: str, user_list: str, password_list: str):
    """Run a hydra command nicely."""
    words = ["hydra"]
    words.extend(["-L", user_list])
    words.extend(["-P", password_list])
    words.extend(interface)
    words.extend(protocol)
    print("words:", words)
    out = subprocess.run(words, capture_output=True)
    print("out:", out)
    return out
