Deployment on Vercel: [https://nba-collections.vercel.app/](https://nba-collections.vercel.app/)

-> Most functionality (registering/logging in users, creating collections, deleting collections) is accessbile on Vercel deployment 

Link to Video
[https://drive.google.com/file/d/15NtEj2Nxh-nf2FH9W0ER5edFFS5A5Z2l/view?usp=sharing](https://drive.google.com/file/d/15NtEj2Nxh-nf2FH9W0ER5edFFS5A5Z2l/view?usp=sharing)

-> Functionality that is demonstrated in the video: Viewing player cards, adding players to collections, logged in users adding players to collections versus regular users being unable to, etc. 

**** API doesn't work when deployed, I've attached a video to showcase the functionality (approved by Chuck on Discord)***

**Q1 Description of your final project idea:**

```
I will create an NBA Player Collection app where users can log on and create collections of their favorite players in the NBA. They will be able to search up players through a search functionality on the home page and be able to add it to their collections. Users can create and delete multiple collections by specifying the size of collections.
```

**Q2 Describe what functionality will only be available to logged-in users:**

```
All users will be able to search players and view statistics. Logged-in users will be able to create, delete, and add players to their collections.
```


**Q3 List and describe at least 4 forms:**

```
CreateCollectionForm: Users are able to create collections, so this form is used to specify the name of the collection and the size of the collection.

ChooseCollectionForm: Users are shown a drop-down form that shows the collections they've created. This form is used to indicate which collection the player should be added to. 

RegistrationForm: This form is used to register a user's credentials, like their username, email, and password. 

LoginForm: This form is used to log in a user based on their pre-registered credentials.
```


**Q4 List and describe your routes/blueprints (don’t need to list all routes/blueprints you may have–just enough for the requirement):**
```
Player Blueprint: the player_detail ("/players/<player_id>/<player_name>") route shows the relevant statistics of the NBA player. Every user can access this page. Logged-in users will be able to add players to their collections in this route.

Collections Blueprint: the collection_view ("/view-collections/<collection_name>"): route  is only accessbile to logged-in users and shows the collections that a user has created. Each collection routes you to the display of all the players in that collection.
```
**Q5 Describe what will be stored/retrieved from MongoDB:**

```
MongoDB stores users credentials in the following document format: 
1. Email
2. Username
3. Hashed password
More importantly, MongoDB stores the collections in the following document format: 
1. The user that created it (unique ID)
2. Collection name
3. Collection size 
4. List of players in that collection

Since collections are only available to logged-in users, MongoDB fetches all collection documents that were created by the given user. Similarly, MongoDB fetches the relevant user given a username and password. 
```
**Q6 Describe what Python package or API you will use and how it will affect the user experience:**
```
The Python API I used during thsi project was nba_api (https://github.com/swar/nba_api). To access images of players, which is not built in, I used the following link: https://cdn.nba.com/headshots/nba/latest/1040x760/{id}.png where the ID's attained from nba_api corresponded to the apporpirate player. This API allowed me to showcase relevant statistics for every player and also create collections of players that they want to add to their fantasy team.
```
