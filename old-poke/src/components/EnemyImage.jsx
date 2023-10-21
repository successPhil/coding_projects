export default function EnemyImage({enemyImage}){
    return (
    <div className="enemy-image">      
    <img src={enemyImage} style={{
      height: '420px',
      width: '100%', // This will make the image take up the full width of its container
      objectFit: 'contain', // This ensures the image is contained within the specified height and width
    }}
    />
    </div>)

}