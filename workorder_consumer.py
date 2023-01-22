import pika, sys, os
import dao as DataAcess

# connects to rabbit MQ on local host server to fetch new work orders    
def fetch_workorder():
    print('fetch workorder')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='workorder')
    def callback(ch, method, properties, body):
        DataAcess.insert_batch(body,'workorder')

    channel.basic_consume(queue='workorder', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


def main():
    fetch_workorder()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)