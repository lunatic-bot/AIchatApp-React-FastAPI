import { Link } from "react-router-dom";

const HomePage = () => {
  return (
    <div className="home-container">
      <h1>Welcome to AI Chat</h1>
      <p>Chat with an AI assistant in real time!</p>
      <Link to="/chat">
        <button className="start-chat-btn">Start Chatting</button>
      </Link>
    </div>
  );
};

export default HomePage;
