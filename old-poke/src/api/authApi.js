import axios from 'axios'

const API_BASE_URL = 'http://localhost:8000';

export async function signupAxios(context) {
  try {
    const response = await axios.post(`${API_BASE_URL}/login/signup`, context, {
      headers: {
        'Content-Type': 'application/json',
      },
    });
    return response.data;
  } catch (error) {
    console.error('Error in signupAxios:', error);
    throw error;
  }
}

export async function loginAxios(context) {
  try {
    const response = await axios.post(`${API_BASE_URL}/login/get-token`, context, {
      headers: {
        'Content-Type': 'application/json',
      },
    });
    return response.data.token;
  } catch (error) {
    console.error('Error in loginAxios:', error);
    throw error;
  }
}

export async function getTrainerPokemon() {
  
  
  try {
    const response = await axios.get(`${API_BASE_URL}/trainer/pokemon`, {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Token ${localStorage.getItem("token")}`,
      },
    });

    return response.data;
  } catch (error) {
    console.error('Error in getTrainerPokemon:', error);
    throw error;
  }
}