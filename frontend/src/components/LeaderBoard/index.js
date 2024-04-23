import React from "react";
import './index.css'
import LeaderBoard from '../LeaderBoardChart'

export default function LeaderBoardTab(props) {
    return (
        <div className="dashTabContainer">
            <div className="listContainer">
                <LeaderBoard />
            </div>
        </div>
    );
}