#!/usr/bin/env python
import pika

# Infrastructure init
from commands.hello_world import HelloWorldCommand
from commands.message_command import MessageCommand

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')

while True:
    # Command Detection
    cmd = input()
    if cmd == "hw":
        command = HelloWorldCommand()
    elif cmd.startswith("msg: "):
        message = cmd.split(" ")[1]
        command = MessageCommand(message)
    else:
        print("ERROR: COMMAND NOT FOUND")
        continue

    # Publish command
    channel.basic_publish(exchange='', routing_key='hello', body=command.serialize())
    print(" [x] Sent 'Hello World!'")

connection.close()
