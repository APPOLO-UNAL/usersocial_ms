# usersocial_ms

Repository with the microservice usersocial for APPOLO software system

## Endpoints

### User

#### Get
Endpoint to retrieve information about an user.
- **GET** `/user/?uid=uid`

#### Create
Endpoint to create a new user.
- **POST** `/user`

#### Update
Endpoint to update information of an existing user.
- **PUT** `/user/?uid=uid`

#### Delete
Endpoint to delete an existing user.
- **DELETE** `/user`
- In body provide the userName of the user you want to delete.

### Search

#### Search all
Endpoint to search all users.
- **GET** `/getAllUsers/`

#### Search by email
Endpoint to search for users based on email Address.
- **GET** `/user/?emailAddr=emailAddr`

#### Search by user name
Endpoint to search for users based on user name.
- **GET** `/user/?userName=userName`

### Update

#### Follow user
Endpoint to follow another user.
- **PUT** `follow/`
- In body provide the uid of the current user in uid1 and the uid of the user you want to follow in uid2.

#### Unfollow user
Endpoint to unfollow another user.
- **PUT** `unfollow/`
- In body provide the uid of the current user in uid1 and the uid of the user you want to unfollow in uid2.

#### Update by email
Endpoint to update information of an existing user by email.
- **PUT** `/user/?emailAddr=emailAddr`

#### Update by user name
Endpoint to update information of an existing user by user name.
- **PUT** `/user/?userName=userName`

## Comands to use this ms

### For neo4j database 
1. go to the DB_UserSocial folder
2. docker network create my-network
3. `docker build -t db_usersocial .`
4. `docker run --network my-network -d --name db_usersocial -p 7474:7474 -p 7687:7687 db_usersocial`
### For django api
1. go to the MS_UserSocial folder
2. `docker build -t ms_usersocial .`
3. `docker run --network my-network -p 8000:8000 -e NEO4J_HOST=db_usersocial -e NEO4J_PORT=7687 -e NEO4J_USER=neo4j -e NEO4J_PASSWORD=password -e URL=0.0.0.0:8000 ms_usersocial`
