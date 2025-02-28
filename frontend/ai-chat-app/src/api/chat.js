import axios from "axios";

export const getChatData = async () => {
  try {
    const response = await axios.get("http://localhost:8000/chat", {
      withCredentials: true, // Ensures cookies (access token) are sent
    });
    return response.data;
  } catch (error) {
    console.error("Failed to fetch chat data:", error);
    throw error;
  }
};
