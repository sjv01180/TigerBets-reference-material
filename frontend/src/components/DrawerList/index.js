import React from "react";
import PropTypes from 'prop-types';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import DashboardIcon from '@mui/icons-material/Dashboard';
import PersonIcon from '@mui/icons-material/Person';

export default function DrawerList(props) {
    const { setTab } = props;
    

    return (
        <List>
            <ListItem disablePadding>
                <ListItemButton onClick={() => setTab(0)}>
                    <ListItemIcon><DashboardIcon style={{color: '#d4601d'}}/></ListItemIcon>
                    <ListItemText primary={"Events"} />
                </ListItemButton>
            </ListItem>
            <ListItem disablePadding>
                <ListItemButton onClick={() => setTab(0)}>
                    <ListItemIcon><DashboardIcon style={{color: '#d4601d'}}/></ListItemIcon>
                    <ListItemText primary={"Current Bets"} />
                </ListItemButton>
            </ListItem>
            <ListItem disablePadding>
                <ListItemButton onClick={() => setTab(0)}>
                    <ListItemIcon><DashboardIcon style={{color: '#d4601d'}}/></ListItemIcon>
                    <ListItemText primary={"Leaderboard"} />
                </ListItemButton>
            </ListItem>
            <ListItem disablePadding>
                <ListItemButton onClick={() => setTab(1)}>
                    <ListItemIcon><PersonIcon style={{color: '#d4601d'}}/></ListItemIcon>
                    <ListItemText primary={"Profile"} />
                </ListItemButton>
            </ListItem>
        </List>
    );
}

DrawerList.propTypes = {
    setTab: PropTypes.func.isRequired
};