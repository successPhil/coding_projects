import { useEffect, useContext } from 'react';
import TrainerContext from '../contexts/TrainerContext';
import { getTrainerPokemon } from '../api/authApi';
import PokeCard from '../muiComponents/PokeCard';
import Grid from '@mui/material/Grid';
import Container from '@mui/material/Container'

export default function TrainerPokes(){

    const token = localStorage.getItem('token')
    const { trainerPokemon, setTrainerPokemon } = useContext(TrainerContext);

    useEffect(() => {
        const fetchTrainerPokemon = async () => {
        if (token) {
            try {
            const data = await getTrainerPokemon();
            setTrainerPokemon(data);
            } catch (error) {
                console.error('Error fetching trainer Pokemon:', error);
            }
        }
        };
    fetchTrainerPokemon()
}, []);


    return (
        <>
        {trainerPokemon ? (
        <Container id='centered-container'>
        <Grid container spacing={2}>
          {trainerPokemon.map(pokemon => (
            <Grid item xs={3} key={pokemon.id}>
              <PokeCard pokemon={pokemon} />
            </Grid>   
          ))}
        </Grid>
        </Container>
     
      ) : (
        <p>Loading...</p>
      )}
    </>
  )
}