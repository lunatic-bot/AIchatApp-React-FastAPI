import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

const HomePage = () => {
  const navigate = useNavigate();
  const [isAuthenticated, setIsAuthenticated] = useState(null);

  // Check auth status from the backend
  useEffect(() => {
    const checkAuthStatus = async () => {
      try {
        const response = await fetch("/auth/status", {
          method: "GET",
          credentials: "include",
        });

        if (response.ok) {
          try {
            const data = await response.json(); // Only parse JSON if response is OK
            if (data.status === "authenticated") {
              setIsAuthenticated(true);
            } else {
              setIsAuthenticated(false);
            }
          } catch (jsonError) {
            console.error("Invalid JSON response:", jsonError);
            setIsAuthenticated(false);
          }
        } else if (response.status === 401) {
          setIsAuthenticated(false);
        }
      } catch (error) {
        console.error("Failed to check auth status:", error);
        setIsAuthenticated(false);
      }
    };

    checkAuthStatus();
  }, []);

  // Handle button click for redirection
  const handleStartChat = () => {
    if (isAuthenticated) {
      navigate("/chat"); // Redirect to chat if authenticated
    } else {
      navigate("/auth/login"); // Redirect to login if not authenticated
    }
  };

  // Show loading state while checking auth status
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
