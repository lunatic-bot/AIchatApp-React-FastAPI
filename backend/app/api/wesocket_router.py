from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from managers.connection_manager import manager
from services.ai_response_service import get_ai_response

websocket_router = APIRouter()

@websocket_router.websocket("/chat/{room_id}")
async def chat_websocket(websocket: WebSocket, room_id: int):
    """WebSocket endpoint for chat with AI bot."""
    await manager.connect(websocket)
    print(f"New connection to room {room_id}")

    try:
        while True:
            user_message = await websocket.receive_text()
            print(f"Received: {user_message}")

            # Broadcast user message to all clients
            await manager.broadcast(f"User: {user_message}")

            # Generate AI response
            ai_response = await get_ai_response(user_message)

            # Send AI response to the user
            await manager.send_message(websocket, f"Bot: {ai_response}")

    except WebSocketDisconnect:
        manager.disconnect(websocket)
        print(f"Disconnected from room {room_id}")
