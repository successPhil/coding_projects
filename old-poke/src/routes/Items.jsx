import { getTrainerItems, updateItems } from "../api/authApi"
import TrainerContext from "../contexts/TrainerContext"
import { useContext, useEffect } from "react"
import TrainerItemsCard from "../muiComponents/TrainerItemsCard"
import Container from "@mui/material/Container"
import Grid from "@mui/material/Grid"


export default function Items() {
    const {selectPokemon, trainerItems, setTrainerItems, itemsUsed} = useContext(TrainerContext)

    const refreshItems = async () => {
        const items = await getTrainerItems()
        setTrainerItems(items)
      }

    useEffect(()=>{
        refreshItems()
    }, [])

    return (
        <>
        {trainerItems ? (
        <Container>
        <Grid container spacing={2} sx={{justifyContent:'center'}}>
          {trainerItems.map(item => (
            <Grid item xs={9} key={item.id}>
              <TrainerItemsCard item={item} isShop={false} />
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