from fastapi import FastAPI
from routes.user import user
from routes.events import event
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.include_router(user)
app.include_router(event)

origins = ["*", "http://localhost:8080/"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)