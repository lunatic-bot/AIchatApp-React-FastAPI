import axios from "axios";

export const loginUser = async (username, password) => {
  try {
    const response = await axios.post(
      "http://localhost:8000/login", // Update with your actual backend URL
      { username, password },
      {
        withCredentials: true, // This ensures cookies are sent & received
      }
    );

    return response.data; // Refresh token (if needed)
  } catch (error) {
    console.error("Login failed:", error.response?.data || error.message);
    throw error;
  }
};
