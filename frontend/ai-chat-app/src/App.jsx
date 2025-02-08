import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import ChatPage from "./components/pages/ChatPage";
import HomePage from "./components/pages/HomePage";
import Navbar from "./components/Navbar";

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/chat" element={<ChatPage />} />
      </Routes>
    </Router>
  );
}

export default App;
