import Message from "./Message";

const ChatBox = ({ messages }) => {
  return (
    <div className="chat-box">
      {messages.map((msg, index) => (
        <Message key={index} text={msg.text} sender={msg.sender} />
      ))}
    </div>
  );
};

export default ChatBox;
