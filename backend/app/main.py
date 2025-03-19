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
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],  # Frontend origin
    allow_credentials=True,  # Allow sending cookies
    allow_methods=["*"],
    allow_headers=["*"],
)



# Include Routers
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(websocket_router, prefix="", tags=["WebSocket"])

