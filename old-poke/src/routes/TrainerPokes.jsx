import { useEffect, useContext } from 'react';
import TrainerContext from '../contexts/TrainerContext';
import { getTrainerPokemon } from '../api/authApi';
import PokeCard from '../muiComponents/PokeCard';

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

  console.log(trainerPokemon, 'THIS IS STATE MOTHER FUCKER')
    return (
        <>
        {trainerPokemon ? (
      trainerPokemon.map(pokemon => (
        <PokeCard key={pokemon.id} pokemon={pokemon} />))) : (<p>Loading...</p>)}
        <h1 className="pokemon-type-icon psychic">wrfwrflwrfl</h1>
        </>
    )
}