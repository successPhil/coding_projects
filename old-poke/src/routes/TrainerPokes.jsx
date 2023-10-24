import { useEffect, useContext, useState } from 'react';
import TrainerContext from '../contexts/TrainerContext';
import { getTrainerPokemon, getFirstPokemon } from '../api/authApi';
import PokeCard from '../muiComponents/PokeCard';
import Grid from '@mui/material/Grid';
import Container from '@mui/material/Container'
import Button from '@mui/material/Button';

export default function TrainerPokes(){

    const token = localStorage.getItem('token')
    const { trainerPokemon, setTrainerPokemon, selectPokemon, setSelectPokemon } = useContext(TrainerContext);
    
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
}, [selectPokemon]);


    


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