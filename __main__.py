#!/usr/bin/env python

import os
import dotenv
import uvicorn

from dotenv import load_dotenv
load_dotenv()

uvicorn.run(
    "web_hydra:app", port=os.environ["PORT"], host=os.environ["HOST"], # reload=True, # reload_dirs=["web-hydra"]
)
