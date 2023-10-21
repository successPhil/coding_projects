import React from 'react';

const MenuButton = ({ label, onClick }) => {
  const buttonStyle = {
    cursor: 'pointer',
    border: 'none',
    background: 'transparent',
    fontFamily: 'Pokemon GB', // Apply your custom font
    fontSize: '2.0rem', // Adjust as needed
    color: '000000', // Adjust color to match your design
  };

  return (
    <button style={buttonStyle} onClick={onClick}>
      {label}
    </button>
  );
};

export default MenuButton;
