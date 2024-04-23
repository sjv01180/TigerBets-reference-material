import React from "react";
import './index.css'
import EventList from '../EventList'

export default function DashboardTab(props) {
    return (
        <div className="dashTabContainer">
            <div className="listContainer">
                <div className="list1"><EventList /></div>
            </div>
        </div>
    );
}