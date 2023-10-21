import Pokeball from "../styles/Pokeball";
import MenuButton from "../styles/MenuButton";

export default function GameMenu({moves, openMoves, toggleMenu}) {

  const handleFightClick = () => {
    console.log('click')
    toggleMenu(openMoves)
  }

  return (
    <div className='gameboy-menu-container'>
      <div className='gameboy-menu-box'>
        <div className='menu-content'>
        <div className="button-row">
        <MenuButton label="FIGHT" onClick={(handleFightClick)}  />
      <MenuButton label="POKE"  />
      </div>
      <div className="button-row">
      <MenuButton label="ITEMS"  />
      <MenuButton label="RUN"  />
      </div>
        </div>
      </div>
      <div className="top-left">
        <Pokeball />
      </div>
      <div className="top-right">
        <Pokeball />
      </div>
      <div className="bottom-left">
        <Pokeball />
      </div>
      <div className="bottom-right">
        <Pokeball />
      </div>
    </div>
  );
}
