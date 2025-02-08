import { Link } from "react-router-dom";

const HomePage = () => {
  return (
    <div className="container d-flex justify-content-center align-items-center vh-100">
      <div className="text-center">
        <h1 className="mb-4">Welcome to AI Chat</h1>
        <Link to="/chat" className="btn btn-primary btn-lg">
          Start Chatting
        </Link>
      </div>
    </div>
  );
};

export default HomePage;
