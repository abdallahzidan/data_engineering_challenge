import pika

# push data to rabbit MQ (on local host) in the given queue
def Push_to_queue(message,queue):
    
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=queue)
    channel.basic_publish(exchange='', routing_key=queue, body=message)
    print(" [x] Sent messsage")
    connection.close()
    

