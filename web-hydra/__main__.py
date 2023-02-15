#!/usr/bin/env python

from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return "Lets get started"


@app.get("/{protocol}/{url}")
def bruteforce(protocol, str, url: str, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
