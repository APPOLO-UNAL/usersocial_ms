# Create a custom Dockerfile based on a Neo4j image:

FROM neo4j:5.17.0-enterprise
COPY extension_script.sh /extension_script.sh
ENV EXTENSION_SCRIPT=/extension_script.sh

# FROM creates a layer from the software Docker image.
# COPY adds files from your Docker client's current directory.
# RUN builds your application with make.
# CMD specifies what command to run within the container.
#------------- Comandos -----------------

# echo "extension logic"

# # Build the custom image:

# docker build --file /example/Dockerfile --tag neo4j:5.17.0-enterprise-custom-container-1 /example

# # Create and run a container based on the custom image:

# docker run --interactive --tty --name custom-container-1 -p7687:7687 -p7474:7474 -p7473:7473 --env NEO4J_AUTH=neo4j/password --env NEO4J_ACCEPT_LICENSE_AGREEMENT=yes neo4j:5.17.0-enterprise-custom-container-1