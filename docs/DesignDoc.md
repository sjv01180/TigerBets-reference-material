
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

### Software Architecture
![architectural-pattern](..%2Fassets%2Farchitectural-pattern.png)

For the software architecture design diagram of “TigerBets”, we adopt a layered approach. From top to bottom, it contains four layers:

**Presentation Layer**: Contains the User Interface (UI) and Simple Visual Charts.

**Application Layer**: Consists of Business Logic, Application Controllers for Authentication (Auth), Events, Accounts, Betting, and Analytics.

**Domain Layer**: Involves Business Rules and Data Analytics, along with Entities such as Event, User, and Bet.

**Persistence Layer:**: Includes the Database for Authentication (Auth), User information, Events, Bets, and the Leaderboard.

Each layer communicates information down to the next, indicating that the upper layers rely on the data and services provided by the lower ones. This architectural design emphasizes separation of concerns, with each layer focusing on specific functionalities to enhance the maintainability and scalability of the software.


### Use Cases
 
![use-case-diagram](..%2Fassets%2Fuse-case-diagram.png)
 
***

**Use Case Detailed Descriptions**

This use case diagram describes two actors in the TigerBets system: regular end users and system administrators. Each has their own functions and use cases. The diagram also illustrates the relationship between these two different actors. 

------

**Actor: End User**

- **Register or Login User**:  Users must log in with their own account to access the main page. If they do not have an account, they need to register a new account that has not been used by other users on the login interface. Once the registration is complete, users can log into the system with their new account.

- **Manage Profile**: After logging into the page, users can fill in or update their personal information on the user information page.

- **View Events**: Users can view the sporting events they are interested in on the event page. 

- **Place Bets and update points**: Users can choose the events they are interested in and place bets on an outcome with points. If the user does not have any points to spend, they will receive an alert message and the event will not accept bets from said user.

- **Update Points**: Once an event has ended, Users who bet on the event will receive additional points depending on the outcome of the event.

- **View Leaderboard**: Users can view the standing of points among all other users through the system's leaderboard

------

**Actor: Admin**

- **Login User**: Different from regular users, administrators have a different login interface. Accounts of regular users cannot log into the administrator's account. Only accounts with administrator privileges can log into the administrator page.

- **View Leaderboard**: Admins can view the standing of points among all end users through the system's leaderboard

- **Manage Users**: Administrators can manage the accounts of end users, such as updating their information and deleting their accounts from the system.

- **Manage Events**: Administrators can update and upload new events, as well as delete events.

 


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
