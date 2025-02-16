from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
from auth import auth_router
from wskt import websocket_router

app = FastAPI(debug=True,
              title="AI-ChatApp",
    summary=None,
    description="",
    version="0.1.0",)


# Include Routers
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(websocket_router, prefix="", tags=["WebSocket"])

