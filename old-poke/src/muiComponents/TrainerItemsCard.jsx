import CardContent from '@mui/material/CardContent';
import Paper from '@mui/material/Paper';
import CardBaloo from '../styles/CardBaloo';
import Button from '@mui/material/Button';
import TrainerContext from '../contexts/TrainerContext';
import { updateItems } from '../api/authApi';
import { useContext, useState} from 'react';
import Select from '@mui/material/Select';
import MenuItem from '@mui/material/MenuItem';
import { useNavigate } from 'react-router-dom';
import { useEffect } from 'react';
import { capitalizeFirst } from '../components/EnemyData';
import { makeTransaction } from '../api/authApi';


export default function TrainerItemsCard({item, isShop }) {
    const {trainer, trainerTurn, endTrainerTurn, selectPokemon, setSelectPokemon, trainerItems, setTrainerItems, itemsUsed, setItemsUsed, setTrainerDialogue, trainerShop, setTrainerShop } = useContext(TrainerContext)
    const [shouldRedirect, setShouldRedirect] = useState(false)
    const navigate = useNavigate()

    useEffect(()=>{
        if (!trainerTurn){
            navigate("/battle")
        }
    }, [trainerTurn])

    useEffect(()=>{
        if (shouldRedirect){
            navigate("/items")
        }
    }, [shouldRedirect])

    const [open, setOpen] = useState(false);

    const handleChange = (event) => {
    setItemsUsed(event.target.value);
    };

    const handleClose = () => {
      setOpen(false);
     };

    const handleOpen = () => {
    setOpen(true);
    };



    const updateTrainerItems = async () => {
        // Find the item to update
        const updatedItem = trainerItems.find(item => item.id === item.id);
    
        if (updatedItem && selectPokemon) {
            // Update the quantity
            updatedItem.quantity -= itemsUsed;
            // Create a new array with the updated item
            const updatedTrainerItems = trainerItems.map(item =>
                item.id === updatedItem.id ? updatedItem : item
            );
            // Set the new state
            setTrainerItems(updatedTrainerItems);
            // Send the update to the backend
            updateItems(item.id, itemsUsed);
            
            const healingAmount = item.stat_boost * itemsUsed
            const missingHealth = selectPokemon.max_health - selectPokemon.health
            const usedHealingAmount = healingAmount > missingHealth ? missingHealth : healingAmount

            const newHealth = selectPokemon.health + healingAmount
            const maxHealth = selectPokemon.max_health
            const updatedHealth = newHealth > maxHealth ? maxHealth : newHealth;
            const itemMsg = `${capitalizeFirst(selectPokemon.name)} has healed ${usedHealingAmount} from using ${itemsUsed} ${item.name}${itemsUsed > 1 ? "s" : ""}! ${capitalizeFirst(selectPokemon.name)} now has ${updatedHealth} health!!!`
            setTrainerDialogue(itemMsg)
            setSelectPokemon((prev) => ({...prev, health: updatedHealth, }))
            endTrainerTurn()
        }
    };

    const updateShopItems = async () => {
        console.log(trainer.money, 'CHECKING MONEY IN ITEM CARD')
        if (trainer.money >= item.value * itemsUsed) {
            const updatedItem = trainerShop.find(item => item.id === item.id);
            if (updatedItem){
                updatedItem.quantity -= itemsUsed;
                const updatedShopItems = trainerShop.map(item =>
                    item.id === updatedItem.id ? updatedItem : item);
                makeTransaction(item, itemsUsed, 'buy')
                console.log('Should have called make transaction')
                setTrainerShop(updatedShopItems)
                setShouldRedirect(true)
            }
        }
    }


    return(
        <>
        <Paper elevation={3} sx={{mt: 8, pt:2, pl:4, pr: 4, height: 100, borderBottomLeftRadius: 15, borderBottomRightRadius: 15, borderTopLeftRadius:15, borderTopRightRadius:15}}>
            <CardContent sx={{display:'flex', justifyContent:'space-between'}}>
                <CardBaloo>{item.name}</CardBaloo>
                <CardBaloo>Quantity: {item.quantity}</CardBaloo>
                <CardBaloo>Value: {item.value}</CardBaloo>
                <Select
                labelId="demo-controlled-open-select-label"
                id="demo-controlled-open-select"
                open={open}
                onClose={handleClose}
                onOpen={handleOpen}
                value={itemsUsed}
                label="Items"
                onChange={handleChange}
                >
{[...Array(item.quantity).keys()].map(i => (
        <MenuItem value={i + 1} key={`amountItem${item.id}${i + 1}`}><span className='item-button-text'>{i + 1}</span></MenuItem>
    ))}
                </Select>
                {!isShop && selectPokemon && <Button variant='contained' color='primary' onClick={updateTrainerItems}><span className='item-button-text'>Use Item</span></Button>}
                {isShop && selectPokemon && <Button variant='contained' color='primary' onClick={updateShopItems}><span className='item-button-text'>Buy Item</span></Button>}
            </CardContent>
        </Paper>

        </>
    )
}