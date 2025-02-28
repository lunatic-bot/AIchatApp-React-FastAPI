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

    try {
      await loginUser(username, password); // Calls the backend login API
      navigate("/chat"); // Redirect after successful login
    } catch (error) {
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

// import { useState } from "react";
// import { useNavigate, Link } from "react-router-dom";

// const LoginPage = () => {
//   const [email, setEmail] = useState("");
//   const [password, setPassword] = useState("");
//   const navigate = useNavigate();

//   // const handleLogin = (e) => {
//   //   e.preventDefault();
//   //   console.log("Logging in:", email);
//   //   navigate("/chat");
//   // };
//   const handleLogin = (e) => {
//     e.preventDefault();
//     console.log("Logging in:", email);

//     // Simulate successful login
//     localStorage.setItem("isAuthenticated", "true");

//     navigate("/chat"); // Redirect to chat
//   };

//   return (
//     <div className="d-flex justify-content-center mt-4 vh-60">
//       <div className="card w-50 p-4">
//         <div className="card-header bg-primary text-white text-center">
//           Login
//         </div>
//         <div className="card-body">
//           <form onSubmit={handleLogin}>
//             <div className="mb-3">
//               <label className="form-label">Email</label>
//               <input
//                 type="email"
//                 className="form-control"
//                 value={email}
//                 onChange={(e) => setEmail(e.target.value)}
//                 required
//               />
//             </div>
//             <div className="mb-3">
//               <label className="form-label">Password</label>
//               <input
//                 type="password"
//                 className="form-control"
//                 value={password}
//                 onChange={(e) => setPassword(e.target.value)}
//                 required
//               />
//             </div>

//             <button type="submit" className="btn btn-primary w-100">
//               Login
//             </button>
//           </form>

//           {/* Forgot Password Link */}
//           <div className="text-center mt-3">
//             <Link to="/forgot-password">Forgot Password?</Link>
//           </div>

//           {/* Register Link */}
//           <div className="text-center mt-2">
//             Don't have an account? <Link to="/register">Create an account</Link>
//           </div>
//         </div>
//       </div>
//     </div>
//   );
// };

// export default LoginPage;
