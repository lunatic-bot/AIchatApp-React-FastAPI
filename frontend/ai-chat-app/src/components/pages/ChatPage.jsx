// import { useEffect } from "react";

// const ChatPage = () => {
//   useEffect(() => {
//     console.log("ChatPage loaded!"); // This should log in the console
//   }, []);

//   return (
//     <div>
//       <h1>Welcome to Chat</h1>
//     </div>
//   );
// };

// export default ChatPage;

import { useState } from "react";

const ChatPage = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const sendMessage = () => {
    if (!input.trim()) return;
    setMessages([...messages, { text: input, sender: "user" }]);
    setInput("");
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter") {
      e.preventDefault(); // Prevents line break in input
      sendMessage();
    }
  };

  return (
    <div className="container mt-4">
      <div className="card">
        <div className="card-header bg-primary text-white">AI Chat</div>
        <div
          className="card-body chat-box"
          style={{ height: "400px", overflowY: "auto" }}
        >
          {messages.map((msg, index) => (
            <div
              key={index}
              className={`p-2 my-2 rounded ${
                msg.sender === "user"
                  ? "bg-light text-end"
                  : "bg-info text-white"
              }`}
            >
              {msg.text}
            </div>
          ))}
        </div>
        <div className="card-footer d-flex">
          <input
            type="text"
            className="form-control"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyPress} // Handles Enter key press
            placeholder="Type a message..."
          />
          <button className="btn btn-success ms-2" onClick={sendMessage}>
            Send
          </button>
        </div>
      </div>
    </div>
  );
};

export default ChatPage;
