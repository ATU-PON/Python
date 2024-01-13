"""
Script: udp_client.py
By: Paul O'Neill
Purpose: This is a UDP client used to simulate temperatures and transmit them
Prerequisites:
Tested: Visual Studio Code under Windows 10

Revision History:
Alpha Version:  November 2023

Notes:

"""
# Below we will tell Python to import the socket, time and random functions from the standard library

import socket
import time
import random
import threading

def send_temperature(sensor_id, server_address, server_port):
    # First we create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        # Here Generate a random temperature between a defined range (0 and 40 degrees Celsius)
        temperature = round(random.uniform(0, 40), 2)

        # We get the current timestamp
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

        # We then combine timestamp, sensor_id, and temperature into a string
        data = f'{timestamp},{sensor_id},{temperature}'

        # We encode the data and send it to the server (yet to be defined)
        client_socket.sendto(data.encode('utf-8'), (server_address, server_port))

        print(f'Sent data from Sensor {sensor_id}: {temperature}°C at {timestamp}')

        # Then wait for 5 seconds before sending the next temperature
        time.sleep(5)

if __name__ == '__main__':
    # Specify the server address and port
    server_address = 'localhost'
    server_port = 12345

    # Start three clients with different sensor IDs using threads
    threads = []
    for sensor_id in range(1, 4):
        thread = threading.Thread(target=send_temperature, args=(sensor_id, server_address, server_port))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()