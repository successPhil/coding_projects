import GameText from "../styles/PokemonGB"
import ProgressBar from "./ProgressBar"
import PlayerBar from "./PlayerBar"
import { capitalizeFirst } from "./EnemyData";

export default function PlayerData({selectName, selectLevel, selectExp, selectTotalXP, selectHealth, selectMaxHealth}){
    const isPlayer = true;
    const upperSelectName = capitalizeFirst(selectName)


    return(<>
    <PlayerBar isPlayer={isPlayer}/>
    <div className="player-name">
    <GameText>{upperSelectName}</GameText>
    </div>
    <div className="player-level">
        <GameText>LVL:{selectLevel}</GameText>
    </div>
    <div className="player-health-bar">
    <GameText>HP: </GameText>
    <ProgressBar  value={selectHealth} maxValue={selectMaxHealth} barColor={'#DA2C38'} />
    </div>
    <div className="player-xp-bar">
    <GameText>XP:</GameText>
    <ProgressBar value={selectExp} maxValue={selectTotalXP} barColor={'#D5E5AE'}/>
    </div>
    </>)
}