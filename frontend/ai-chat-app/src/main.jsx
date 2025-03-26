import { StrictMode } from "react";
import { createRoot } from "react-dom/client"; // Imports the new root API for rendering in React 18+
import App from "./App.jsx"; // Imports the main App component

// Selects the root DOM element where the React app will be mounted
const rootElement = document.getElementById("root");

// Creates a root and renders the application inside React.StrictMode
createRoot(rootElement).render(
  <StrictMode>
    <App /> {/* Renders the main App component inside StrictMode */}
  </StrictMode>
);
