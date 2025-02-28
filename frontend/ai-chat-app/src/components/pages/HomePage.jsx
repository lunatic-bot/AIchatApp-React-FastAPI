import { useNavigate } from "react-router-dom";

const HomePage = () => {
  const navigate = useNavigate();
  const isAuthenticated = localStorage.getItem("isAuthenticated"); // Check login state

  const handleStartChat = () => {
    if (isAuthenticated) {
      navigate("/chat"); // Go to chat if logged in
    } else {
      navigate("/login"); // Otherwise, go to login page
    }
  };

  return (
    <div className="container d-flex justify-content-center align-items-center vh-100">
      <div className="text-center">
        <h1 className="mb-4">Welcome to AI Chat</h1>
        <button onClick={handleStartChat} className="btn btn-primary btn-lg">
          Start Chatting
        </button>
      </div>
    </div>
  );
};

export default HomePage;
