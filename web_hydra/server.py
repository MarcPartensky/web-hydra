#!/usr/bin/env python

from typing import Union

from fastapi import FastAPI

app = FastAPI()

front_folder = "./front/dist"


@app.get("/")
def index():
    return "Lets get started"


@app.get("/{protocol}/{url}")
def bruteforce(protocol: str, url: str, q: Union[str, None] = None):
    return {"protocol": protocol, "url": url, "q": q}
