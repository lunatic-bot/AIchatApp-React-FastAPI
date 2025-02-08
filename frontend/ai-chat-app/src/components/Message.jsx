const Message = ({ text, sender }) => {
  return (
    <div className={`message ${sender === "bot" ? "bot" : "user"}`}>
      <p>{text}</p>
    </div>
  );
};

export default Message;
