#!/usr/bin/env python
import pika, sys, os
import time
import random

from commands.hello_world import HelloWorldCommand
from commands.message_command import MessageCommand


def main():
    # initialization
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')

    def choose_command(ch, method, properties, body):
        body = body.decode('utf-8')
        if body == "HWC":
            command = HelloWorldCommand.deserialize(body)
        elif body.startswith("MC: "):
            command = MessageCommand.deserialize(body)
        else:
            print("ERROR: COMMAND NOT FOUND")
            return
        command.execute()

    channel.basic_consume(queue='hello', on_message_callback=choose_command, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
