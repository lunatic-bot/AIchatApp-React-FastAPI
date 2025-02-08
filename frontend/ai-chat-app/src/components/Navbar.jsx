import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <nav className="navbar">
      <h2>AI Chat</h2>
      <ul>
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/chat">Chat</Link>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;
