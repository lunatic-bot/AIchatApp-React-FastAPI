import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

const HomePage = () => {
  const navigate = useNavigate();
  const [isAuthenticated, setIsAuthenticated] = useState(null); // null initially to prevent premature redirects

  useEffect(() => {
    fetch("/auth/status", {
      method: "GET",
      credentials: "include", // Include HTTP-only cookies
    })
      .then((response) => {
        if (response.ok) {
          setIsAuthenticated(true);
        } else {
          setIsAuthenticated(false);
        }
      })
      .catch((error) => {
        console.error("Error checking auth status:", error);
        setIsAuthenticated(false);
      });
  }, []);

  useEffect(() => {
    if (isAuthenticated === false) {
      navigate("/login");
    }
  }, [isAuthenticated, navigate]);

  if (isAuthenticated === null) {
    return <div>Loading...</div>; // Prevent redirect flicker
  }

  return (
    <div className="container d-flex justify-content-center align-items-center vh-100">
      <div className="text-center">
        <h1 className="mb-4">Welcome to AI Chat</h1>
        <button
          onClick={() => navigate("/chat")}
          className="btn btn-primary btn-lg"
        >
          Start Chatting
        </button>
      </div>
    </div>
  );
};

export default HomePage;
