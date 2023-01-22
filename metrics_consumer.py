import pika, sys, os
import dao as DataAcess

def fetch_metrics():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='metrics')

    def callback(ch, method, properties, body):
        #print(" [x] Received %r" % body)
        print(" [x] Received")
        DataAcess.insert_batch(body,'metrics')

    channel.basic_consume(queue='metrics', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    

def main():
    fetch_metrics()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)