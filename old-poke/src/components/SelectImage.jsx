import { motion } from "framer-motion"
import {  useContext } from "react"
import TrainerContext from "../contexts/TrainerContext"
import Pokeball from "../styles/Pokeball"
export default function SelectImage({selectImage}){
    const { animateSelect, animateSelectAttack } = useContext(TrainerContext)
    // console.log(animateSelect, 'in select image')
    return (<>
        <motion.div
        className="select-image"
        initial={{x:0, y:0}}
        animate={animateSelect ? { x: 200, y: -130, rotate: 30 } : { x: 0, y: 0, rotate: 0 }}
        transition={{ duration: 0.4 }} // Adjust the duration as needed 
        >      
        <img src={selectImage} style={{
          height: '420px',
          width: '100%', // This will make the image take up the full width of its container
          objectFit: 'contain', // This ensures the image is contained within the specified height and width
        }}
        />
        </motion.div>
        </>
        
        )
}