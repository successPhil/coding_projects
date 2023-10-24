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

export async function getTrainerPokemon(id=null) {
  let url = `${API_BASE_URL}/trainer/pokemon`

  if (id != null){
    url += `/${id}`
  }
  try {
    const response = await axios.get(url, {
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

export async function getEnemyPokemon(){
  try {
    let url = `${API_BASE_URL}/trainer/enemy-poke`
    const response = await axios.get(url, {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Token ${localStorage.getItem("token")}`
      },
    })

    return response.data
  }
  catch (error) {
    console.error('Error in getEnemyPokemon:', error)
    throw error;
  }
}

export async function getFirstPokemon(){
  try {
    let url = `${API_BASE_URL}/trainer/first-poke`
    
    const response = await axios.get(url, {
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Token ${localStorage.getItem("token")}`
      },
    })

    return response.data
  } catch (error) {
    console.error('Error in getFirstPokemon', error)
    throw error
  }
  }

  export async function updateBattleResults(selectPokemon, battle_result, money, experience) {
    try {
      const trainerData = {
        trainer_data: {
          pokemon_id: selectPokemon.id,
          current_health: selectPokemon.health,
          experience: experience,
          battle_result: battle_result,
          money: money,
        }
      };

      const response = await axios.put(`${API_BASE_URL}/trainer/battleResults`, trainerData, {
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Token ${localStorage.getItem("token")}`,
        },
      });
    
  
      return response.data;
    } catch (error) {
      console.error('Error in updateBattleResults:', error);
      throw error;
    }
  }
  