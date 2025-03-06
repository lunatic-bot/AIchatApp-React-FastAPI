import Message from "./Message"; // Import the Message component to display individual messages

/**
 * ChatBox Component
 * Renders a list of chat messages inside a container.
 *
 * @param {Object} props - Component props
 * @param {Array} props.messages - An array of message objects, each containing `text` and `sender`
 * @returns {JSX.Element} A chat box displaying all messages
 */
const ChatBox = ({ messages }) => {
  return (
    <div className="chat-box">
      {" "}
      {/* Container for the chat messages */}
      {messages.map((msg, index) => (
        <Message key={index} text={msg.text} sender={msg.sender} />
        // Render each message using the Message component
      ))}
    </div>
  );
};

export default ChatBox; // Export the ChatBox component for use in other parts of the app
