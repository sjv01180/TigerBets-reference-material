import React, { useState } from "react";
import { useNavigate } from 'react-router-dom';
import { Button, Tab, Tabs, TextField } from "@mui/material";
import { LOGIN_IMAGE_URL } from '../../constants'
import "./index.css"

export default function Login() {
    const navigate = useNavigate();
    const [currentTabIndex, setCurrentTabIndex] = useState(0);

    const handleTabChange = (e, tabIndex) => {
        console.log(tabIndex);
        setCurrentTabIndex(tabIndex);
      };

    const handleLoginOnClick = () => {
        // fill in with login API
        // navigate to dashboard screen
        navigate('/dashboard');
    }

    const handleRegisterOnClick = () => {
        // fill in with register API
        // navigate to dashboard screen
        navigate('/dashboard');
    }

    return (
        <div className="container">
            <div className="subContainer"> 
                <img src={LOGIN_IMAGE_URL} alt="login page" className="image"/>
                <div className="footer">Disclaimer: TigerBets operates solely with a friendly point system and does not involve real money transactions. The platform is intended for entertainment purposes only</div>
            </div>
            <div className="tabContainer">
                <div className="title">Tiger Bets</div>
                <Tabs value={currentTabIndex} onChange={handleTabChange} centered>
                    <Tab label='Login' style={{color: "#465098"}}/>
                    <Tab label='Register' style={{color: "#465098"}}/>
                </Tabs>
                {/* TAB 1 Contents */}
                {currentTabIndex === 0 && (
                    <div className="tab">
                        <TextField label="Email" variant="outlined" size="small" fullWidth margin="normal" required/>
                        <TextField label="Password" variant="outlined" size="small" fullWidth margin="normal" required type="password"/>
                        <Button style={{backgroundColor: "#F76900", marginTop: "1rem"}} variant="contained" margin="normal" fullWidth onClick={handleLoginOnClick}>LOGIN</Button>
                        <div className="tabFooter">Don't have an account? Register</div>
                    </div>
                )}
                {/* TAB 2 Contents */}
                {currentTabIndex === 1 && (
                    <div className="tab">
                        <TextField label="Name" variant="outlined" size="small" fullWidth margin="normal" required/>
                        <TextField label="Email" variant="outlined" size="small" fullWidth margin="normal" required/>
                        <TextField label="Phone" variant="outlined" size="small" fullWidth margin="normal" required/>
                        <TextField label="Password" variant="outlined" size="small" fullWidth margin="normal" required type="password"/>
                        <Button style={{backgroundColor: "#F76900", marginTop: "1rem"}} variant="contained" margin="normal" fullWidth onClick={handleRegisterOnClick}>REGISTER</Button>
                        <div className="tabFooter">Already have an account? Login</div>
                    </div>
                )}
            </div>

        </div>
    );
    }
    
