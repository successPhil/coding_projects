import TrainerContext from "../contexts/TrainerContext"
import { useContext, useEffect } from "react"
import TrainerItemsCard from "../muiComponents/TrainerItemsCard"
import Container from "@mui/material/Container"
import Paper from "@mui/material/Paper"
import Grid from "@mui/material/Grid"
import { getTrainer, getTrainerShop } from "../api/authApi"
import GameText from "../styles/PokemonGB"


export default function Shop(){
    const {trainerShop, setTrainerShop , trainer, setTrainer, itemsUsed } = useContext(TrainerContext)
    const getUserTrainer = async () => {
        const userTrainer = await getTrainer()
        setTrainer(userTrainer)
      }
    
    const getUserShop = async () => {
        const shop = await getTrainerShop()
        setTrainerShop(shop)
      }
   
    console.log(trainerShop, 'INSIDE TRAINER SHOP')

    useEffect(()=>{
        getUserTrainer()
        getUserShop()
    }, [])

    return (
        <>
        {trainerShop && trainer ? (
        <Container>
            <Grid container sx={{justifyContent: 'center', alignItems: 'center'}}>
            <Grid item xs={4}>
            <Paper sx={{height: 63, mt:2, pt:2, pl:3, pr:2}}>
            <GameText>KO coins: {trainer.money}</GameText>
            </Paper>
            </Grid>
            </Grid>
        <Grid container spacing={2} sx={{justifyContent:'center'}}>
            
          {trainerShop.map(item => (
            <Grid item xs={9} key={item.id}>
                
              <TrainerItemsCard item={item} isShop={true} />
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