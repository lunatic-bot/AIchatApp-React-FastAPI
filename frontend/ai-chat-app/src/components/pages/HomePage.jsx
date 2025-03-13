import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

const HomePage = () => {
  const navigate = useNavigate();
  const [isAuthenticated, setIsAuthenticated] = useState(null); // null = unknown state

  useEffect(() => {
    // Fetch authentication status from the backend
    const checkAuthStatus = async () => {
      try {
        const response = await fetch("/auth/status", {
          method: "GET",
          credentials: "include", // Send cookies
        });
        console.log(response.status);
        if (response.ok) {
          setIsAuthenticated(true); // User is authenticated
        } else if (response.status === 401) {
          setIsAuthenticated(false); // User is not authenticated
        }
      } catch (error) {
        console.error("Error checking auth status:", error);
        setIsAuthenticated(false); // Treat network errors as unauthenticated
      }
    };

    checkAuthStatus();
  }, []);

  console.log(isAuthenticated);
  // Handle the "Start Chatting" button click
  const handleStartChat = () => {
    if (isAuthenticated) {
      navigate("/chat"); // If logged in → go to chat
    } else {
      navigate("/auth/login"); // If not logged in → go to login
    }
  };

  // Show loading while status is being checked
  if (isAuthenticated === null) {
    return <div>Loading...</div>;
  }

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
