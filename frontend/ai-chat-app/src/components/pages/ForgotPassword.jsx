import { useState } from "react";
import { useNavigate } from "react-router-dom";

const ForgotPassword = () => {
  const [email, setEmail] = useState("");
  const [message, setMessage] = useState("");
  const navigate = useNavigate();

  const handleForgotPassword = async (e) => {
    e.preventDefault();

    // Simulate sending request to backend
    console.log("Sending password reset link to:", email);

    // Here, you would make an API call to send the reset link
    setMessage(
      "If an account exists with this email, a reset link has been sent."
    );

    // Optionally, navigate back to login after some time
    setTimeout(() => navigate("/login"), 3000);
  };

  return (
    <div className="d-flex justify-content-center mt-4 vh-60">
      <div className="card w-50 p-4">
        <div className="card-header bg-primary text-dark text-center">
          Forgot Password
        </div>
        <div className="card-body">
          <form onSubmit={handleForgotPassword}>
            <div className="mb-3">
              <label className="form-label">Enter your Email</label>
              <input
                type="email"
                className="form-control"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
              />
            </div>

            <button type="submit" className="btn btn-primary w-100">
              Send Reset Link
            </button>
          </form>

          {message && <div className="alert alert-info mt-3">{message}</div>}
        </div>
      </div>
    </div>
  );
};

export default ForgotPassword;
