import { useState, useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";

/**
 * Navbar Component
 * Displays navigation links and handles user authentication status.
 */
const Navbar = () => {
  const [user, setUser] = useState(null); // Stores the logged-in user's name
  const navigate = useNavigate(); // Hook for navigation

  // Check if the user is logged in when the component mounts
  useEffect(() => {
    const checkLoginStatus = async () => {
      try {
        const response = await fetch("http://localhost:8000/auth/status", {
          credentials: "include", // Send cookies with request
        });

        if (response.ok) {
          const data = await response.json();
          setUser(data.user); // Assuming the backend returns { "user": "username" }
        } else {
          setUser(null);
        }
      } catch (error) {
        console.error("Error checking login status:", error);
      }
    };

    checkLoginStatus();
  }, []);

  // Logout function to handle user logout
  const handleLogout = async () => {
    try {
      await fetch("http://localhost:8000/auth/logout", {
        method: "POST",
        credentials: "include", // Send cookies with request
      });

      setUser(null); // Clear user state
      navigate("/login"); // Redirect to login page
    } catch (error) {
      console.error("Logout failed:", error);
    }
  };

  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
      <div className="container-fluid">
        {/* Brand logo linking to home */}
        <Link className="navbar-brand" to="/">
          AI Chat
        </Link>
        <div className="collapse navbar-collapse">
          <ul className="navbar-nav ms-auto">
            {/* Chat link */}
            <li className="nav-item">
              <Link className="nav-link" to="/chat">
                Chat
              </Link>
            </li>

            {/* Show different options based on login status */}
            {user ? (
              <>
                <li className="nav-item">
                  <span className="nav-link">Welcome, {user}!</span>
                </li>
                <li className="nav-item">
                  <button className="btn btn-danger" onClick={handleLogout}>
                    Logout
                  </button>
                </li>
              </>
            ) : (
              <>
                {/* Show login and register links if user is not logged in */}
                <li className="nav-item">
                  <Link className="nav-link" to="/login">
                    Login
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/register">
                    Register
                  </Link>
                </li>
              </>
            )}
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
// export
