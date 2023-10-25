import GameMenu from "../components/GameMenu"
import GameDialogue from "../components/GameDialogue"
import PlayerData from "../components/PlayerData"
import EnemyData from "../components/EnemyData"
import MovesList from "../components/MovesList"
import GetEnemyButton from "../components/GetEnemyButton"
import RewardBox from "../components/RewardBox"
import TrainerContext from "../contexts/TrainerContext"
import { useContext, useState, useEffect } from "react"
import { capitalizeFirst } from "../components/EnemyData"
import { updateBattleResults, getEnemyPokemon, getFirstPokemon } from "../api/authApi"


export default function Trainer(){ 
    const { trainerPokemon, trainerTurn, endTrainerTurn, endEnemyTurn, enemyPokemon, setEnemyPokemon, selectPokemon, setSelectPokemon, enemyDialogue, setEnemyDialogue, trainerDialogue, setTrainerDialogue,victoryMsg, setVictoryMsg, rewardDialogue, setRewardDialogue, typeMultipliers, setAnimateSelect, setAnimateEnemy } = useContext(TrainerContext);
    const [ openMoves, setOpenMoves ] = useState(false)
    const [ showRewards, setShowRewards ] = useState(false)

    const clearEnemy = (resultMessage) => {
        setEnemyPokemon(null)
        setShowRewards(true)
        setEnemyDialogue(resultMessage)
    }

    const clearSelect = (lose_msg) => {
        setSelectPokemon(null)
        setEnemyDialogue(lose_msg)
    }

    const hideRewards = () => {
        setShowRewards(false)
    }

    const animateSelectAttack = () => {
        setAnimateSelect(true)
        setTimeout(() => {
            setAnimateSelect(false);
        }, 400); // Adjust the duration as needed 
    }

    const animateEnemyAttack = () => {
        setAnimateEnemy(true)
        setTimeout(() => {
            setAnimateEnemy(false);
        }, 400); // Adjust the duration as needed 
    }

    const chooseEnemy = (pokemon) => {
        const enemyStr = `A wild ${pokemon.name} has appeared!`
        setEnemyDialogue(enemyStr)
        setEnemyPokemon(pokemon)
    }

    async function fetchEnemy() {
        if (!enemyPokemon){
            const enemy = await getEnemyPokemon()
            chooseEnemy(enemy)
        }
        }

    const firstPoke = async () => {
      
        console.log(trainerPokemon)
        if (!trainerPokemon || trainerPokemon.length === 0){
            const starterPoke = await getFirstPokemon()
            const firstPokeMsg = `You received a ${capitalizeFirst(starterPoke.name)}!`
            console.log(firstPokeMsg, 'testing message')
            setEnemyDialogue(firstPokeMsg)
            setSelectPokemon(starterPoke)
        }
    }


    useEffect(() => {
        firstPoke()
    }, [])

    const calculateType = (attackPokemon, attackMove, defensePokemon) => {
        const defenseTypeList = defensePokemon.types.split(", ")
        const attackTypeList = attackPokemon.types.split(", ")
        let pokemonBonus = 1
        let moveBonus = 1

        for (const type of defenseTypeList){
            let bonusList = typeMultipliers[type]

            for (const type of attackTypeList){
                if (bonusList.doubleDamageFrom.includes(type)){
                    pokemonBonus *=2
                }
                if (bonusList.halfDamageFrom.includes(type)){
                    pokemonBonus *= 0.5
                }
                if (bonusList.doubleDamageFrom.includes(attackMove.type)){
                    moveBonus *= 2
                }
                if (bonusList.halfDamageFrom.includes(attackMove.type)){
                    moveBonus *= 0.5
                }

            }
        }
        console.log(pokemonBonus, 'this is the poke bonus')
        console.log(moveBonus, 'this is the move bonus')
        return {pokemonBonus, moveBonus}
    }


// resultMessage we added to update results field with data from updateBattle
    async function updateBattle(selectPokemon, battleResults, money, experience, resultMessage) {
        if (battleResults == 'win'){
            const updated = await updateBattleResults(selectPokemon, battleResults, money, experience)
            setSelectPokemon(updated)
            clearEnemy(resultMessage)
        } else {
            clearSelect(resultMessage)
            updateBattleResults(selectPokemon, battleResults, experience, money)
        }
    }

    console.log(trainerTurn)
  
    const toggleMenu = (prev) => {setOpenMoves(!prev)}

    const testAttack = (enemyPokemon, selectPokemon) => {
        enemyAttack(enemyPokemon, selectPokemon)
    }

    const selectRandomMove = (moves) => {
        const randomIndex = Math.floor(Math.random() * moves.length);
        return moves[randomIndex];
      }

    

    const playerAttack = async (selectPokemon, move, enemyPokemon) => {
    const randomMultiplier = Math.floor(Math.random() * 5) + 2; // Generates a random integer between 2 and 6
    const {pokemonBonus, moveBonus } = calculateType(selectPokemon, move, enemyPokemon) //Order matters - attacking poke, move being used, defending poke
    const bonus = pokemonBonus * moveBonus
    const basePokemonDamage = Math.ceil(selectPokemon.power * pokemonBonus)
    const baseMoveDamage = Math.floor((move.damage * moveBonus * randomMultiplier))
    const baseDamage = basePokemonDamage + baseMoveDamage
    const baseDefense = Math.ceil((selectPokemon.power / 5) + selectPokemon.defense)
    let damage = 1
    if (baseDamage < baseDefense){
        damage = baseDamage
    } else {
        damage = baseDamage - baseDefense
    }
    console.log(damage, 'CALCULATED DAMAGE')
    let bonusStr = ""
    if (bonus > 1){
        bonusStr = "It's super effective!!!"
    }
    if (bonus < 1){
        bonusStr = "It's not very effective..."
    }

    if (enemyPokemon.health - parseInt(damage) <= 0){
        const money = (selectPokemon.level * selectPokemon.power) + (enemyPokemon.level +  enemyPokemon.power)
        const experience = selectPokemon.level * selectPokemon.power
        const victory_msg = `${capitalizeFirst(selectPokemon.name)} has defeated ${capitalizeFirst(enemyPokemon.name)} in battle! ${capitalizeFirst(enemyPokemon.name)} has been added to your inventory of Pokemon.`
        const rewardMessage = `${capitalizeFirst(selectPokemon.name)} has gained ${experience} exp from battle! You have gained ${money} KO coins!!`
        updateBattle(selectPokemon, 'win', money, experience, victory_msg)
        setVictoryMsg(victory_msg)
        setRewardDialogue(rewardMessage)
        animateSelectAttack()
    } else {
        const attack_msg = `${capitalizeFirst(selectPokemon.name)} used ${capitalizeFirst(move.name)} on ${capitalizeFirst(enemyPokemon.name)} dealing ${damage} damage! ${bonusStr}`
        const after_attack = enemyPokemon
        after_attack.health -= damage
        setEnemyPokemon(after_attack)
        setTrainerDialogue(attack_msg)
       animateSelectAttack()
        
        endTrainerTurn()
    }
    return damage;
    };
   

    const enemyAttack = async (enemyPokemon, selectPokemon) => {
        if (!selectPokemon){
            endEnemyTurn()
        }
      
    if (enemyPokemon && selectPokemon){
        const move = selectRandomMove(enemyPokemon.moves)
        const randomMultiplier = Math.floor(Math.random() * 5) + 2;
        const {pokemonBonus, moveBonus } = calculateType(enemyPokemon, move, selectPokemon)
        const bonus = pokemonBonus * moveBonus
        const basePokemonDamage = Math.ceil(enemyPokemon.power * pokemonBonus)
        const baseMoveDamage = Math.floor((move.damage * moveBonus * randomMultiplier))
        const baseDamage = basePokemonDamage + baseMoveDamage
        const baseDefense = Math.ceil((selectPokemon.power / 5) + selectPokemon.defense)
        let damage = 1
        if (baseDamage < baseDefense){
            damage = baseDamage
        } else {
            damage = baseDamage - baseDefense
        }
        console.log(damage)
        let bonusStr = ""
        if (bonus > 1){
            bonusStr = "It's super effective!!!"
        }
        if (bonus < 1){
            bonusStr = "It's not very effective..."
        }

        const attackMessage = `${capitalizeFirst(enemyPokemon.name)} used ${capitalizeFirst(move.name)} on ${capitalizeFirst(selectPokemon.name)} dealing ${damage} damage! ${bonusStr}`
        const resultMessage = `${capitalizeFirst(selectPokemon.name)} has been defeated by ${capitalizeFirst(enemyPokemon.name)}! ${capitalizeFirst(selectPokemon.name)} storms off in a hurry!`


        if (selectPokemon.health - parseInt(damage)<= 0){
            updateBattle(selectPokemon, 'lose', 100, 0, resultMessage)
        }
        else {
            setSelectPokemon(prevSelectPokemon => ({
                ...prevSelectPokemon,
                health: prevSelectPokemon.health - damage}))
            setEnemyDialogue(attackMessage);
        }

        await new Promise(resolve => setTimeout(resolve, 2000)); // Add a delay to simulate the attack animation
        
        endEnemyTurn();
    }
    }

    useEffect(() => {
        if (!trainerTurn ) {
            const timeout = setTimeout(() => {
                if (enemyPokemon && selectPokemon){
                    enemyAttack(enemyPokemon, selectPokemon);
                    animateEnemyAttack()
                }
            }, 5000);
            return () => clearTimeout(timeout); // Cleanup the timeout on component cleanup
        }
    }, [trainerTurn])




    return (
        <>
        <button onClick={()=> testAttack(enemyPokemon, selectPokemon)}>MO TESTIN</button>
        <button onClick={firstPoke}>MAYBE THIS WORKS</button>
        {showRewards && 
        <div onClick={hideRewards}>
          <RewardBox text={rewardDialogue}/>
          </div>
        }
      
        {!enemyPokemon && 
        <div onClick={fetchEnemy}>
        <GetEnemyButton getEnemy={true}/>
        </div>
        }
        
        {selectPokemon && (
        <PlayerData
            selectPokemon={selectPokemon}
        />
        )}
        {enemyPokemon && (
        <EnemyData
            enemyPokemon={enemyPokemon}
        />
        )}
        {!enemyPokemon && trainerTurn && <GameDialogue text={victoryMsg} />}
        {trainerTurn && enemyPokemon && <GameDialogue text={enemyDialogue} />}
        {trainerTurn && !enemyPokemon && <GameDialogue text={enemyDialogue} />}
        {!trainerTurn && <GameDialogue text={trainerDialogue} />}
        {selectPokemon && <GameMenu moves={selectPokemon.moves} toggleMenu={toggleMenu} openMoves={openMoves} />}
        {selectPokemon && openMoves && (
        <MovesList
            moves={selectPokemon.moves}
            endTrainerTurn={endTrainerTurn}
            trainerTurn={trainerTurn}
            toggleMenu={toggleMenu}
            openMoves={openMoves}
            selectPokemon={selectPokemon}
            trainerDialogue={trainerDialogue}
            setTrainerDialogue={setTrainerDialogue}
            enemyPokemon={enemyPokemon}
            playerAttack={playerAttack}
        />
        )}
    </>
    );
}