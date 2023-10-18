import { BrowserRouter as Router, Routes, Route } from "react-router-dom"
import Login from "./routes/Login"
import Trainer from './components/Trainer'
import ResponsiveAppBar from "./muiComponents/AppBar"
import TrainerPokes from "./routes/TrainerPokes"
import Shop from "./routes/Shop"
import Items from "./routes/Items"
import TrainerContext from "./contexts/TrainerContext"
import { useState, useEffect } from "react"

function App() {
  const [formData, setFormData] = useState({ username: '', password: '' });
  const [userToken, setUserToken] = useState(null)
  const [checked, setChecked] = useState(false)
  const [signUp, setSignUp ] = useState(false)
  const [trainerPokemon, setTrainerPokemon] = useState([]);
  const [trainerItems, setTrainerItems] = useState([]);
  const [trainerStore, setTrainerStore] = useState([]);


  useEffect( () => {
    const token = localStorage.getItem("token")
    if(token) {
      setUserToken(token)
    }
  }, [])

  

  const handleToken = (token) => {
    setFormData({ username: '', password: '' })
    localStorage.setItem("token", token)
    setUserToken(token)
  }
  
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleOnClick = (prev) => {
    setChecked(!prev);
  }

  const handleSignUp = () => {
    setSignUp(true)
  }

  const handleLogout = () => {
    var keyToRemove = 'token';
  localStorage.removeItem(keyToRemove);
  setUserToken(false)
  setSignUp(false)
  }

  try {
    const token = localStorage.getItem("token");
    console.log("Token from local storage:", token);
  } catch (error) {
    console.error("Error accessing local storage:", error);
  }

  return (
    <>
    <TrainerContext.Provider value={{userToken, trainerPokemon, setTrainerPokemon}}>
      <Router>
      <ResponsiveAppBar handleLogout={handleLogout} />
        <Routes>
          <Route path="/" element={<Login checked={checked} handleOnClick={handleOnClick} handleInputChange={handleInputChange} formData={formData} handleToken={handleToken} token={userToken} signUp={signUp} handleSignUp={handleSignUp}/>} />
          <Route path="pokemon" element={<TrainerPokes />} />
          <Route path="battle" element={<Trainer />} />
          <Route path="shop" element={<Shop />} />
          <Route path="items" element={<Items />} />
        </Routes>
      </Router>
      </TrainerContext.Provider>
    </>
  )
}

export default App
