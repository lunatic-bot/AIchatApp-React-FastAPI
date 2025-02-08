import { useState, useEffect } from "react";
import ChatBox from "../ChatBox";
import ChatInput from "../ChatInput";

const ChatPage = () => {
  const [messages, setMessages] = useState([]);
  const [socket, setSocket] = useState(null);

  useEffect(() => {
    const ws = new WebSocket("ws://localhost:8000/chat/1"); // Adjust URL based on backend
    setSocket(ws);

    ws.onmessage = (event) => {
      const newMessage = { text: event.data, sender: "bot" };
      setMessages((prev) => [...prev, newMessage]);
    };

    return () => ws.close();
  }, []);

  const sendMessage = (message) => {
    if (socket) {
      socket.send(message);
      setMessages((prev) => [...prev, { text: message, sender: "user" }]);
    }
  };

  return (
    <div className="chat-container">
      <ChatBox messages={messages} />
      <ChatInput sendMessage={sendMessage} />
    </div>
  );
};

export default ChatPage;
