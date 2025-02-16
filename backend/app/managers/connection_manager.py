from fastapi import WebSocket, WebSocketDisconnect
from typing import List

class ConnectionManager:
    """Handles WebSocket connections and broadcasting."""
    
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        """Accept and store WebSocket connections."""
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        """Remove disconnected WebSocket connections."""
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        """Send messages to all active WebSocket clients."""
        for connection in self.active_connections:
            try:
                await connection.send_text(message)
            except WebSocketDisconnect:
                self.disconnect(connection)

    async def send_message(self, websocket: WebSocket, message: str):
        """Send a message to a specific WebSocket client."""
        await websocket.send_text(message)

# Singleton instance of ConnectionManager
manager = ConnectionManager()
