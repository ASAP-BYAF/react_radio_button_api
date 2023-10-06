from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routers import task, file

app = FastAPI()
app.include_router(task.router)
app.include_router(file.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)
