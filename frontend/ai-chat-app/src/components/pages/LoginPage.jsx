import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";

const LoginPage = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleLogin = (e) => {
    e.preventDefault();
    console.log("Logging in:", email);
    navigate("/chat");
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
              <label className="form-label">Email</label>
              <input
                type="email"
                className="form-control"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
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

            <button type="submit" className="btn btn-primary w-100">
              Login
            </button>
          </form>

          {/* Forgot Password Link */}
          <div className="text-center mt-3">
            <Link to="/forgot-password">Forgot Password?</Link>
          </div>

          {/* Register Link */}
          <div className="text-center mt-2">
            Don't have an account? <Link to="/register">Create an account</Link>
          </div>
        </div>
      </div>
    </div>
  );
};

export default LoginPage;
