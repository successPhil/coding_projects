import GameText from "./PokemonGB"
import TrainerContext from "../contexts/TrainerContext";
import { useContext } from "react";
import { capitalizeFirst } from "../components/EnemyData";
export default function MovesListItem({move, toggleTurn, trainerTurn, toggleMenu, openMoves}){
    const upperMove = capitalizeFirst(move.name)
    const { typeToClassname, typeToIcon, moveInfo, setMoveInfo} = useContext(TrainerContext);
    const typeClassName = typeToClassname[move.type];
    const icon = typeToIcon[move.type];
    const iconClassName = 'pokemon-type-icon'
    


    const handleClickMove = (move) => {
        setMoveInfo([move.name, move.damage])
        toggleTurn(trainerTurn)
        toggleMenu(openMoves)
    }

    return (
    <>
       <div className='gameboy-move-box' onClick={()=> handleClickMove(move)}>
        <div className='move-content' >
       <div className={`${iconClassName} ${typeClassName}`} >{icon}</div><GameText component='div' >{upperMove}</GameText>
        </div>
      </div>
    </>)

}