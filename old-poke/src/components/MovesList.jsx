import Pokeball from "../styles/Pokeball";
import MovesListItem from "../styles/MovesListItem";
export default function MovesList({moves, toggleTurn, trainerTurn, toggleMenu, openMoves}) {
    return (<div className="gameboy-moves-container">
    <div className='gameboy-move-container'>
        {moves.map((move) => (<MovesListItem move={move} key={move.id} toggleTurn={toggleTurn} trainerTurn={trainerTurn} toggleMenu={toggleMenu} openMoves={openMoves}/>))}
    </div>
    <div className="top-left-menu">
        <Pokeball />
      </div>
      <div className="top-right-menu">
        <Pokeball />
      </div>
      <div className="bottom-left-menu">
        <Pokeball />
      </div>
      <div className="bottom-right-menu">
        <Pokeball />
      </div>

    </div>)
}