import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import ChatPage from "./components/pages/ChatPage";
import HomePage from "./components/pages/HomePage";
import RegisterPage from "./components/pages/RegisterPage";
import LoginPage from "./components/pages/LoginPage";
import Navbar from "./components/Navbar";
import "bootstrap/dist/css/bootstrap.min.css";

function App() {
  return (
    <Router>
      <div className="app-container">
        <Navbar />
        <div className="content">
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/chat" element={<ChatPage />} />
            <Route path="/register" element={<RegisterPage />} />
            <Route path="/login" element={<LoginPage />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;

// import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
// import ChatPage from "./components/pages/ChatPage";
// import HomePage from "./components/pages/HomePage";
// import Navbar from "./components/Navbar";
// import "bootstrap/dist/css/bootstrap.min.css";

// function App() {
//   return (
//     <Router>
//       <div className="app-container">
//         <Navbar />
//         <div className="content">
//           <Routes>
//             <Route path="/" element={<HomePage />} />
//             <Route path="/chat" element={<ChatPage />} />
//           </Routes>
//         </div>
//       </div>
//     </Router>
//   );
// }

// export default App;
