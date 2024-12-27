import axios from 'axios';

export const fetchTrends = async (location = 'US') => {
  try {
    // Pass the location as a query parameter
    const response = await axios.get(`http://localhost:5001/api/trends?location=${location}`);
    if (response.status === 200) {
      return response.data; // Return the trends data
    } else {
      throw new Error(`Unexpected response code: ${response.status}`);
    }
  } catch (error) {
    console.error("Error fetching trends:", error);
    throw error; // Re-throw the error for further handling
  }
};

export const categorizeTrends = async (trends) => {
  try {
    const response = await axios.post('http://localhost:5001/api/categorize', { trends });
    return response.data.categories; // Return parsed categories
  } catch (error) {
    console.error("Error categorizing trends:", error);
    throw error;
  }
};