
# PROJECT Design Documentation

> _The following template provides the headings for your Design
> Documentation.  As you edit each section make sure you remove these
> commentary 'blockquotes'; the lines that start with a > character
> and appear in the generated PDF in italics._

## Team Information
* Team name: TigerBets
* Team members
  - Chen, Weijie, wxc2710
  - Liu, Xu, xl8302
  - Velasquez, Samuel, sjv5866
  - Vellaisamy Senthilkumar, Rohini, rv8542


## Executive Summary

This is a summary of the project.


## Requirements

This section describes the features of the application.

### Definition of MVP

Our MVP is a platform designed for betting on events, featuring role-based access and authorization for users. Administrators have control over event management and user accounts, while users can create profiles, navigate events, and place bets. The platform supports point betting and provides basic user analytics, with a leaderboard showcasing top performers. Data is securely stored for persistence, ensuring a smooth user experience.

### MVP Features

- **Role-based Access and Authorization**: Users are granted access and permissions based on their designated roles, ensuring appropriate levels of control within the platform.
Event Management by Admin: Administrators have the capability to create, update, and delete events, maintaining control over the platform's betting opportunities.
- **High-level Account Management**: Administrators are equipped to oversee and manage user accounts at a strategic level, ensuring smooth operation of the platform.
- **User Profile Management**: Users have the ability to create and manage their profiles, customizing their experience within the platform.
- **Event Listing**: Users can easily navigate and find events through filtering and search functionalities, streamlining their experience.
- **Point Betting Capabilities**: Users are empowered to place bets by adding or removing points from a target event, engaging actively in the betting process.
- **Points Management**: Following the conclusion of an event, the platform handles point distribution and adjustment in accordance with the outcomes.
- **Simple User Analytics**: The platform maintains a detailed history of point transactions, win-loss rates, and engagement of activities among all user accounts. These analytics will be displayed for each individual user with visual representations to ensure transparency and accountability among active users.
- **Leaderboard for Top Point Holders**: A leaderboard showcases users with the highest accumulated points, fostering competition and engagement within the community.
- **Persistent Data Storage in Database**: Data persistence is ensured through secure storage in a database, safeguarding information and enabling seamless user experiences.


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
