import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { loginUser } from "../../api/login"; // Importing API function for login requests

function LoginPage() {
  // State variables for username, password, and error messages
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate(); // Hook for programmatic navigation

  // Function to handle form submission
  const handleLogin = async (e) => {
    e.preventDefault(); // Prevents the default form submission behavior
    console.log("Login Button clicked");

    try {
      // Send login request with username and password
      const response = await loginUser(username, password);
      console.log("Login successful:", response); // Log API response

      localStorage.setItem("isAuthenticated", "true"); // Store authentication status in local storage
      navigate("/chat"); // Redirect user to the chat page after successful login
    } catch (error) {
      console.error("Login error:", error.response?.data || error.message);
      setError("Invalid username or password"); // Display error message if login fails
    }
  };

  return (
    <div className="d-flex justify-content-center mt-4 vh-60">
      <div className="card w-50 p-4">
        {/* Card Header */}
        <div className="card-header bg-primary text-white text-center">
          Login
        </div>
        {/* Card Body */}
        <div className="card-body">
          <form onSubmit={handleLogin}>
            {/* Username Input */}
            <div className="mb-3">
              <label className="form-label">Username</label>
              <input
                type="text"
                className="form-control"
                value={username}
                onChange={(e) => setUsername(e.target.value)} // Update state on input change
                required
              />
            </div>
            {/* Password Input */}
            <div className="mb-3">
              <label className="form-label">Password</label>
              <input
                type="password"
                className="form-control"
                value={password}
                onChange={(e) => setPassword(e.target.value)} // Update state on input change
                required
              />
            </div>

            {/* Error Message */}
            {error && <div className="alert alert-danger">{error}</div>}

            {/* Submit Button */}
            <button type="submit" className="btn btn-primary w-100">
              Login
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}

export default LoginPage;
