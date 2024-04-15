# Tiger Bets

[![codecov](https://codecov.io/gh/SWEN-732-G3/TigerBets/graph/badge.svg?token=MGD5UEG2OE)](https://codecov.io/gh/SWEN-732-G3/TigerBets) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=SWEN-732-G3_TigerBets&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=SWEN-732-G3_TigerBets)

TigerBets is an online betting platform designed to provide users with an interactive experience in predicting outcomes across various college sporting events. Our MVP will offer a range of features to cater to both administrators and users, ensuring smooth operation and engaging gameplay. In addition, the platform will provide basic user analytics, a system-wide leaderboard, and persistant data storage to ensure a robust user experience and a friendly competitive environment.

_Disclaimer: TigerBets operates solely with a friendly point system and does not involve real money transactions. The platform is intended for entertainment purposes only._


## Team Information
* Team name: TigerBets
* Team members
  * Rohini Senthilkumar (rohinivsenthil)
  * Samuel Velasquez (sjv01180)
  * Weijie Chen (wxc2710)
  * Xu Liu (xuliugame)


## Documentation

Our project is documented at each phase, ensuring clarity and accessibility for all stakeholders and users.This documentation serves as a reliable reference for understanding the project's progression, facilitating seamless collaboration and knowledge sharing among team members.

Read our [Design Documentation](https://github.com/SWEN-732-G3/TigerBets/blob/main/docs/DesignDoc.md) for more details on the architecture and application design.


## Minimum Requirements

- Python v3.9.18
- Node v21.6.1
- npm v10.2.4
- pip v23.0.1

_Note: Additional requirements for backend are handled with `requirements.txt` by pip, and for frontend with `package.json` by npm._

## How to run it

### Backend

1. Navigate to backend repository
```bash
cd backend
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

2. Run server
```bash
python src/server.py
```

### Frontend

1. Navigate to frontend repository
```bash
cd frontend
```

2. Install dependencies
```bash
npm i
```

2. Run application
```bash
npm start
```

## Testing

Our project uses Python's [unittest](https://docs.python.org/3/library/unittest.html) for unit testing. 

To run unit tests,

1. Navigate to backend repository
```bash
cd backend
```

2. Execute Tests
```bash
python -m unittest -v
```

3. View Coverage
```bash
coverage run -m unittest discover tests
coverage report -m
```

<center><img src="%2Fassets%2Ftesting.png" width="500"></center>
