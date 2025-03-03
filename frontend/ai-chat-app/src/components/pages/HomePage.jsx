import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

const HomePage = () => {
  const navigate = useNavigate();
  const [isAuthenticated, setIsAuthenticated] = useState(null); // Initially null to avoid unnecessary redirects

  useEffect(() => {
    // Fetch authentication status from the backend
    fetch("/auth/status", {
      method: "GET",
      credentials: "include", // Ensures cookies (such as session tokens) are sent
    })
      .then((response) => {
        if (response.ok) {
          setIsAuthenticated(true); // User is authenticated
        } else {
          setIsAuthenticated(false); // User is not authenticated
        }
      })
      .catch((error) => {
        console.error("Error checking auth status:", error);
        setIsAuthenticated(false); // Assume unauthenticated on error
      });
  }, []);

  useEffect(() => {
    // Redirect to login page if authentication fails
    if (isAuthenticated === false) {
      navigate("/login");
    }
  }, [isAuthenticated, navigate]);

  // Show a loading message while authentication status is being determined
  if (isAuthenticated === null) {
    return <div>Loading...</div>; // Prevents flickering due to premature redirects
  }

  return (
    <div className="container d-flex justify-content-center align-items-center vh-100">
      <div className="text-center">
        <h1 className="mb-4">Welcome to AI Chat</h1>
        <button
          onClick={() => navigate("/chat")} // Navigate to chat page when clicked
          className="btn btn-primary btn-lg"
        >
          Start Chatting
        </button>
      </div>
    </div>
  );
};

export default HomePage;
