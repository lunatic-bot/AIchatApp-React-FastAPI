from fastapi import FastAPI
from api.user import auth_router
from api.wesocket_router import websocket_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(debug=True,
              title="AI-ChatApp",
    summary=None,
    description="",
    version="0.1.0",)

##
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],  # Adjust based on your frontend
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


# Include Routers
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(websocket_router, prefix="", tags=["WebSocket"])

