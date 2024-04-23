export const DRAWER_WIDTH = 240;
export const LOGIN_IMAGE_URL = "https://i.ibb.co/hsSWGBh/Screenshot-2024-04-04-at-10-41-34-AM-removebg-preview.png";

export const generateEvent = (date, name, location, pot) => ({
    date,
    name,
    location,
    Pot: pot
});

export const events = [
    generateEvent("04/23 5:00PM", "RIT vs BU Hockey Men", "RIT", 625),
    generateEvent("04/23 8:00PM", "RIT vs BU Hockey Women", "RIT", 340),
    generateEvent("04/25 8:00PM", "RIT vs SU Hockey Men", "SU", 28),
    generateEvent("04/30 5:00PM", "RIT vs RFC Hockey Men", "RIT", 90),
    generateEvent("05/03 7:00PM", "RIT vs NYS Hockey Men", "RIT", 84),
    generateEvent("05/05 5:00PM", "RIT vs RFC Hockey Women", "RIT", 100),
    generateEvent("05/23 5:00PM", "RIT vs BU Hockey Men", "BU", 125),
    generateEvent("05/23 8:00PM", "RIT vs BU Hockey Women", "BU", 100),
    generateEvent("05/28 5:00PM", "RIT vs GFD Hockey Men", "RIT", 0)
];