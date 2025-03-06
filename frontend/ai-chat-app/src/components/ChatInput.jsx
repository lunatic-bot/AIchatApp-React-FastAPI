import { useState } from "react"; // Import useState for managing input state

/**
 * ChatInput Component
 * Provides an input field for users to type messages and send them.
 *
 * @param {Object} props - Component props
 * @param {Function} props.sendMessage - Function to send a message when triggered
 * @returns {JSX.Element} Input field and send button for chat
 */
const ChatInput = ({ sendMessage }) => {
  const [message, setMessage] = useState(""); // State to track user input

  /**
   * Handles sending the message.
   * - Trims the message to prevent empty submissions.
   * - Calls the sendMessage function and clears the input field.
   */
  const handleSend = () => {
    if (message.trim()) {
      sendMessage(message);
      setMessage(""); // Reset input field after sending
    }
  };

  return (
    <div className="chat-input">
      {" "}
      {/* Container for input field and button */}
      <input
        type="text"
        placeholder="Type a message..." // Placeholder text for user guidance
        value={message} // Bind input field to message state
        onChange={(e) => setMessage(e.target.value)} // Update state on user input
      />
      <button onClick={handleSend}>Send</button>{" "}
      {/* Button to send the message */}
    </div>
  );
};

export default ChatInput; // Export the ChatInput component for use in chat
