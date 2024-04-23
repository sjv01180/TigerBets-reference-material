import React from "react";
import './index.css'
import EditIcon from '@mui/icons-material/Edit';
import Button from '@mui/material/Button';

export default function CurrentBetTab(props) {
    return (
        <div className="dashTabContainer">
            <div className="listContainer">
                <div className="card">
                    <div className="teams">
                        <img alt="team-1" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRHCct_C4WnhmoYs6hvRLtxUZPSgkkK6UamO-Rx2qqfCg&s" wdith="80px" height="80px"/>
                        <div><b>vs.</b></div>
                        <img alt="team-2" src="https://www.rit.edu/studentaffairs/sportscamps/assets/images/event_description/RIT-W.jpg" wdith="80px" height="80px"/>
                    </div>
                    <div className="betDetails">
                        You bet 45 points 
                    </div>
                    <div className="live">
                        <div className="live-text">LIVE</div>
                        <Button style={{backgroundColor: '#F76900', color: 'white', fontSize: 'x-small', width: '100%', fontWeight: 'bold', height: '40%', marginTop: '2rem'}} startIcon={<EditIcon/>}>Update Betting</Button>
                    </div>
                </div>
            </div>
        </div>
    )
}