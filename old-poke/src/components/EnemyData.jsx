import GameText from "../styles/PokemonGB"
import ProgressBar from "./ProgressBar"
import PlayerBar from "./PlayerBar"

export function capitalizeFirst(name){
    return name[0].toUpperCase() + name.slice(1)

}

export default function EnemyData({enemyHealth, enemyMaxHealth, enemyName, enemyLevel}) {
    const upperEnemyName = capitalizeFirst(enemyName)
    return (
    <>
    <PlayerBar /> 
    <div className="enemy-name">
        <GameText>{upperEnemyName}</GameText>
    </div>
    <div className="enemy-level">
        <GameText>LVL:{enemyLevel}</GameText>
    </div>
    <div className="enemy-health-bar">
    <GameText>HP:</GameText>
    <ProgressBar value={enemyHealth} maxValue={enemyMaxHealth} barColor={'#DA2C38'} />
    </div>
    </>)
    
}

