from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routers import task, file, appearing, appearing_detail, search

app = FastAPI()
app.include_router(task.router)
app.include_router(file.router)
app.include_router(appearing.router)
app.include_router(appearing_detail.router)
app.include_router(search.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)
