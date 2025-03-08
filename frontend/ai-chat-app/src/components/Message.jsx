/**
 * Message Component
 * Displays a chat message with appropriate styling based on the sender.
 *
 * @param {Object} props - Component props
 * @param {string} props.text - The message text to display
 * @param {string} props.sender - The sender of the message ("bot" or "user")
 * @returns {JSX.Element} A styled message component
 */
const Message = ({ text, sender }) => {
  return (
    <div className={`message ${sender === "bot" ? "bot" : "user"}`}>
      {/* Message text is displayed inside a paragraph tag */}
      <p>{text}</p>
    </div>
  );
};

export default Message; // Export the Message component for use in chat
