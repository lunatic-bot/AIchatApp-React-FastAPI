import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate,
} from "react-router-dom";
import ChatPage from "./components/pages/ChatPage";
import HomePage from "./components/pages/HomePage";
import RegisterPage from "./components/pages/RegisterPage";
import LoginPage from "./components/pages/LoginPage";
import Navbar from "./components/Navbar";
import "bootstrap/dist/css/bootstrap.min.css";
import ForgotPassword from "./components/pages/ForgotPassword";

/**
 * PrivateRoute Component
 * Redirects users to the login page if they are not authenticated.
 */
const PrivateRoute = ({ element }) => {
  const isAuthenticated = localStorage.getItem("isAuthenticated"); // Check authentication status
  return isAuthenticated ? element : <Navigate to="/login" />; // Redirect if not authenticated
};

/**
 * Main Application Component
 * Handles routing and layout of the app.
 */
function App() {
  return (
    <Router>
      <div className="app-container">
        {/* Navbar component (visible on all pages) */}
        <Navbar />
        <div className="content">
          <Routes>
            {/* Public Routes */}
            <Route path="/" element={<HomePage />} />
            <Route path="/register" element={<RegisterPage />} />
            <Route path="/login" element={<LoginPage />} />
            <Route path="/forgot-password" element={<ForgotPassword />} />

            {/* Protected Route (Chat Page) - Requires authentication */}
            <Route
              path="/chat"
              element={<PrivateRoute element={<ChatPage />} />}
            />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
