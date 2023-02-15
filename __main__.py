import uvicorn

uvicorn.run(
    "web-hydra:app", port=80, host="0.0.0.0", reload=True, reload_dirs=["web-hydra"]
)
