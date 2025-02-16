from fastapi import FastAPI
from api.user import auth_router
from api.wesocket_router import websocket_router

app = FastAPI(debug=True,
              title="AI-ChatApp",
    summary=None,
    description="",
    version="0.1.0",)


# Include Routers
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(websocket_router, prefix="", tags=["WebSocket"])

