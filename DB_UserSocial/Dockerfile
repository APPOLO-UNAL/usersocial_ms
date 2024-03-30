# Create a custom Dockerfile based on a Neo4j image:

FROM neo4j:5.17.0-community
ENV NEO4J_AUTH=neo4j/password
ENV dbms.connector.bolt.listen_address: 7687
ENV dbms.connector.bolt.advertised_address: 7687

#----------comandos------------
##Construir la imagen
    #docker build -t db_usersocial .

##Correr la imagen en contenedor
    #docker run -d --name db_usersocial -p 7474:7474 -p 7687:7687 db_usersocial