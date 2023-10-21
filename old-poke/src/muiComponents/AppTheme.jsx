import { createTheme } from '@mui/material/styles';
// #cddddd
// #8d86c9nice purple
// #cacfcd nice background grey
// #cef7a0 grass green color
// #cdeded nice background light blue
// #EFFFC8 nice beige yellow

const AppTheme = createTheme({
  palette: {
    primary: {
      main: '#2f1a4a', // Dark purple
    },
    secondary: {
      main: '#8d86c9', // Pokémon Logo Light Blue
    },
    background: {
      default: '#23282D', // White background for contrast
      paper: '#8d86c9',
      secondary: '#ffffff', // A light gray background for other elements
    },
  },
});

export default AppTheme;
