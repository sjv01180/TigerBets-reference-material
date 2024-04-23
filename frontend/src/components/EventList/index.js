import React from "react";
import './index.css'
import IconButton from '@mui/material/IconButton';
import TurnedInIcon from '@mui/icons-material/TurnedIn';
import {events} from '../../constants'
import TollIcon from '@mui/icons-material/Toll';
import WhatshotIcon from '@mui/icons-material/Whatshot';

export default function EventList(props) {
    return (
        <div className="table">
            <div className="tableTitle">Events List</div>
            <div className="tableHeading">
                <div className="tableHeadingContent">Date/Time</div>
                <div className="tableHeadingContent">Name</div>
                <div className="tableHeadingContent">Location</div>
                <div className="tableHeadingContent">Pot</div>
                <div className="tableHeadingContent">Actions</div>
            </div>
            {events.map((item) => (
                <div className="tableData" key={`${item.date}-${item.name}`}>
                    <div className="tableDataContent">{item.date}</div>
                    <div className="tableDataContent">{item.name}</div>
                    <div className="tableDataContent">
                        <div className={`tableDataCategory-${item.category}`}>{item.location}</div>
                    </div>
                    <div className="tableDataContent">
                        {item.Pot} points
                        {item.Pot >= 100 ? <WhatshotIcon fontSize="small" style={{marginLeft: '.5rem', color: 'F76900'}}/> : <div/> }
                    </div>
                    <div className="tableActions">
                        <IconButton aria-label="edit" style={{padding: 0}} onClick={() => {}}>
                            <TollIcon fontSize="small"/>
                        </IconButton>
                        <IconButton aria-label="delete" style={{padding: 0, marginLeft: '.5rem'}} onClick={() => {}}>
                            <TurnedInIcon fontSize="small"/>
                        </IconButton>
                    </div>
                </div>
            ))}

        </div>);
}