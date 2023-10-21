import GameMenu from "./GameMenu"
import GameDialogue from "./GameDialogue"
import PlayerData from "./PlayerData"
import EnemyData from "./EnemyData"
import EnemyImage from "./EnemyImage"
import SelectImage from "./SelectImage"
import MovesList from "./MovesList"
import { getEnemyPokemon } from "../api/authApi"
import TrainerContext from "../contexts/TrainerContext"
import { useContext, useState } from "react"
import { capitalizeFirst } from "./EnemyData"


export default function Trainer(){ 
    const { enemyPokemon, setEnemyPokemon, selectPokemon, moveInfo } = useContext(TrainerContext);
    const [ trainerTurn , setTrainerTurn ] = useState(true)
    const [ openMoves, setOpenMoves ] = useState(false)

    let trainerDialogue = "";


    const toggleTurn = (prev) => {setTrainerTurn(!prev)}
    const toggleMenu = (prev) => {setOpenMoves(!prev)}

    
    async function getBattlePoke () {
        try {
            const data = await getEnemyPokemon()
            return data
        } catch (error) {
            console.error('Error in getEnemyPoke:', error)
            throw error
        }
    }
    if (enemyPokemon == null){
       getBattlePoke().then(pokemon => {
        if (pokemon) {
            setEnemyPokemon(pokemon)
        }
       }).catch(error => {
        console.error('error in getBattlePoke', error)
        throw error
       })     
    }

    if (selectPokemon) {
        trainerDialogue = `${capitalizeFirst(selectPokemon.name)} used ${moveInfo[0]} on ${capitalizeFirst(enemyPokemon.name)} dealing ${moveInfo[1]} damage!`
    }
  
    console.log(trainerTurn, 'TRAINER TURN')
    console.log(moveInfo, 'MOVE INFO IN APP')
    console.log(openMoves, 'OPEN MOVES')
   

 

    return (<>
    {enemyPokemon && <EnemyImage enemyImage={enemyPokemon.front_image_url}/>}
    {selectPokemon && <SelectImage selectImage={selectPokemon.back_image_url}/>}
    {selectPokemon && <PlayerData selectName={selectPokemon.name} selectLevel={selectPokemon.level} selectHealth={selectPokemon.health} selectMaxHealth={selectPokemon.max_health} selectExp={selectPokemon.experience} selectTotalXP={selectPokemon.totalXP}/>}
    {enemyPokemon && <EnemyData enemyHealth={enemyPokemon.health} enemyMaxHealth={enemyPokemon.max_health} enemyName={enemyPokemon.name} enemyLevel={enemyPokemon.level}/>}
    {trainerTurn ? (<GameDialogue text={trainerDialogue}/>) : ( <GameDialogue text=""/> )}
    {selectPokemon && <GameMenu moves={selectPokemon.moves} toggleMenu={toggleMenu} openMoves={openMoves} />}
    {openMoves && <MovesList moves={selectPokemon.moves} toggleTurn={toggleTurn} trainerTurn={trainerTurn} toggleMenu={toggleMenu} openMoves={openMoves}  />}
     </>
    )
}