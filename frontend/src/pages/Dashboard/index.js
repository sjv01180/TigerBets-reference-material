import React, { useState } from "react";
import Box from '@mui/material/Box';
import Drawer from '@mui/material/Drawer';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Divider from '@mui/material/Divider';
import DrawerList from '../../components/DrawerList'
import DashboardTab from '../../components/DashboardTab'
import ProfileTab from '../../components/ProfileTab'
import Button from '@mui/material/Button';
import LogoutIcon from '@mui/icons-material/Logout';
import { DRAWER_WIDTH } from '../../constants'
import "./index.css"

export default function Dashboard() {
    const [tab, setTab] = useState(0);
    
    return (
            <Box sx={{ display: 'flex' }}>
                <AppBar position="fixed" sx={{ width: `calc(100% - ${DRAWER_WIDTH}px)`, ml: `${DRAWER_WIDTH}px` }}>
                    { tab === 0? 
                    <Toolbar style={{backgroundColor: "#F08000", display: 'flex', justifyContent: 'space-between'}}>
                        <div className="toolBarTitle">Your TigerBets Dashboard</div>
                        <div style={{width: '40%', display: 'flex', justifyContent: 'flex-end'}}>
                        </div>
                    </Toolbar>
                    :
                    <Toolbar style={{backgroundColor: "#F08000", display: 'flex', justifyContent: 'space-between'}}>
                        <div className="toolBarTitle">Your TigerBets Profile</div>
                        <div style={{width: '40%', display: 'flex', justifyContent: 'flex-end'}}>
                            <Button style={{backgroundColor: 'whitesmoke', color: '#d4601d', fontSize: 'x-small', width: '35%', fontWeight: 'bold', marginRight: '1rem'}} startIcon={<LogoutIcon/>}> Logout</Button>
                        </div>
                    </Toolbar>
                    }
                </AppBar>
                <Drawer sx={{ width: DRAWER_WIDTH, flexShrink: 0, display: 'block', '& .MuiDrawer-paper': { width: DRAWER_WIDTH, boxSizing: 'border-box'}}} variant="permanent" anchor="left" >
                    <Toolbar style={{backgroundColor: '#FBCEB1'}} />
                    <Divider />
                    <DrawerList setTab={setTab}/>
                </Drawer>
                { tab === 0 ?
                <div className="mainContainer">
                    <DashboardTab />
                </div>
                :
                <div className="mainContainer">
                    <ProfileTab/>
                </div>
                }
            </Box>
    );
}