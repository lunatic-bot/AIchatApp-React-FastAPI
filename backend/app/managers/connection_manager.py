from fastapi import WebSocket, WebSocketDisconnect  # Import WebSocket handling utilities from FastAPI
from typing import List  # Import List type hint for type annotation

class ConnectionManager:
    """Handles WebSocket connections and broadcasting."""

    def __init__(self):
        """Initialize the connection manager with an empty list of active connections."""
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        """Accept and store WebSocket connections.

        Args:
            websocket (WebSocket): The WebSocket connection to be accepted.
        """
        await websocket.accept()  # Accept the WebSocket connection
        self.active_connections.append(websocket)  # Add the connection to the active list

    def disconnect(self, websocket: WebSocket):
        """Remove disconnected WebSocket connections.

        Args:
            websocket (WebSocket): The WebSocket connection to be removed.
        """
        self.active_connections.remove(websocket)  # Remove the connection from the active list

    async def broadcast(self, message: str):
        """Send a message to all active WebSocket clients.

        Args:
            message (str): The message to broadcast.
        """
        for connection in self.active_connections:
            try:
                await connection.send_text(message)  # Send message to the client
            except WebSocketDisconnect:
                self.disconnect(connection)  # Remove disconnected clients

    async def send_message(self, websocket: WebSocket, message: str):
        """Send a message to a specific WebSocket client.

        Args:
            websocket (WebSocket): The target WebSocket connection.
            message (str): The message to send.
        """
        await websocket.send_text(message)  # Send message to the specified client

# Singleton instance of ConnectionManager to manage WebSocket connections globally
manager = ConnectionManager()
