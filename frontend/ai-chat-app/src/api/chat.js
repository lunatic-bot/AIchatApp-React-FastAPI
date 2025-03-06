import axios from "axios";  // Import Axios for making HTTP requests

/**
 * Fetches chat data from the backend API.
 * 
 * @returns {Promise<Object>} The chat data retrieved from the server.
 * @throws {Error} Throws an error if the request fails.
 */
export const getChatData = async () => {
  try {
    const response = await axios.get("http://localhost:8000/chat", {
      withCredentials: true, // Ensures cookies (e.g., access token) are sent with the request
    });
    
    return response.data;  // Return the fetched chat data
  } catch (error) {
    console.error("Failed to fetch chat data:", error);  // Log the error for debugging
    throw error;  // Re-throw the error to be handled by the caller
  }
};
