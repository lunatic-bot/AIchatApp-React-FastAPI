import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { loginUser } from "../../api/login";

function LoginPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    console.log("Login Button clicked");

    try {
      const response = await loginUser(username, password);
      console.log("Login successful:", response); // Log API response

      localStorage.setItem("isAuthenticated", "true"); // Save auth state
      navigate("/chat"); // Redirect after successful login
    } catch (error) {
      console.error("Login error:", error.response?.data || error.message);
      setError("Invalid username or password");
    }
  };

  return (
    <div className="d-flex justify-content-center mt-4 vh-60">
      <div className="card w-50 p-4">
        <div className="card-header bg-primary text-white text-center">
          Login
        </div>
        <div className="card-body">
          <form onSubmit={handleLogin}>
            <div className="mb-3">
              <label className="form-label">Username</label>
              <input
                type="text"
                className="form-control"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                required
              />
            </div>
            <div className="mb-3">
              <label className="form-label">Password</label>
              <input
                type="password"
                className="form-control"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
            </div>

            {error && <div className="alert alert-danger">{error}</div>}

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
