import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import AppTheme from './muiComponents/AppTheme.jsx'
import { ThemeProvider } from "@emotion/react"
import { CssBaseline } from "@mui/material"

ReactDOM.createRoot(document.getElementById('root')).render(
    <ThemeProvider theme={AppTheme}>
        <CssBaseline/>
        <App />
    </ThemeProvider>
)
