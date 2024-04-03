import pika
import json
import os

def send(title, body, id_user):    
    
    # Crear un diccionario con el objeto JSON
    message = {
        "title": title,
        "message": body,
        "id_user": id_user
    }

    # Convertir el diccionario a una cadena JSON
    jsonBody = json.dumps(message)
    print("Jsonnnnn", jsonBody)
    credentials = pika.PlainCredentials('guest', 'guest')
    host = 'my-rabbit'
    #host = "localhost"
    #print("es la conexión?")
    #print(host)
    parameters = pika.ConnectionParameters(host, 5672, '/', credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    #print("al parecer")

   # Declarar una cola
    queue_name = 'notifications'
    channel.queue_declare(queue=queue_name)

    # Publicar el mensaje en la cola
    channel.basic_publish(
        exchange='',          # Intercambio (Exchange)
        routing_key=queue_name,  # Clave de enrutamiento
        body=jsonBody,        # Cuerpo del mensaje
        properties=pika.BasicProperties(
            content_type='application/json'  # Tipo de contenido
        )
    )
    print(f" [x] Sent {body}")
    connection.close()

#send("Title", "Body", "1")