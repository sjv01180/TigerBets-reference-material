
# PROJECT Design Documentation

> _The following template provides the headings for your Design
> Documentation.  As you edit each section make sure you remove these
> commentary 'blockquotes'; the lines that start with a > character
> and appear in the generated PDF in italics._

## Team Information
* Team name: TEAMNAME
* Team members
  * MEMBER1
  * MEMBER2
  * MEMBER3
  * MEMBER4

## Executive Summary

This is a summary of the project.


## Requirements

This section describes the features of the application.

### Definition of MVP
> _Provide a simple description of the Minimum Viable Product._

### MVP Features
>  _Provide a list of top-level Epics and/or Stories of the MVP._


## Architecture and Design

This section describes the application architecture.

### Software Architecture
> _Place a architectural diagram here._
> _Describe your software architecture._


### Use Cases
> _Place a use case diagram here._
> _Describe your use case diagram._


### Class Diagram
![class-diagram.png](..%2Fassets%2Fclass-diagram.png)
***
This class diagram describes a betting system with several interconnected classes, illustrating the associations between classes and defines the roles each class handles. It also illustrates one-to-many relationships between User and Bet, User and Leaderboard, and Event and Bet. The relationship between User and Profile is depicted as one-to-one, indicating that each user has one profile.

**Description of the diagram**:
**Description of the diagram**:
- **Profile Class**: The Preference field stores user preferences for the application, such as betting options. The userID field contains a direct relationship to the User class, signifying that each profile is associated with a unique user.
- **User Class**: Describes a user with fields for userID, username, password, and points. It has methods for managing user profiles, checking the leaderboard, and placing bets. This is the central entity that connects to the Profile, Bet, and Leaderboard classes, indicating that users have profiles, can participate in betting, and have standings on the leaderboard.
- **Bet Class**: Includes fields such as betID, userID, eventID, and result. The result field is a Boolean, which indicates whether the bet was won or lost. This class is associated with the User and Event classes, where a user can have multiple bets, and each bet is linked to a specific event.
- **Event Class**: Contains event-specific information with fields for eventID and eventName, as well as a method getEvent() to retrieve event details. The multiplicity between Event and Bet indicates that an event can have many bets associated with it.
- **Leaderboard Class**: The Leaderboard class contains getRanking() method where it retrieves the standings of users based on their points.
- **Administrator Class**: Maintains its role with methods manageEvent() and manageUser(), indicating the administrative capabilities to the events within the application and to manage user accounts.
- **AccountManager Class**: Handle account-related operations with methods createUser(), updateUser(), and deleteUser(). This class contains account management operations that can be performed under administrative privileges.
