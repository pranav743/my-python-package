import socket
import pickle
from .colors import *

def send_message(ip, port, data):

    '''This function takes ip, port and data (in the form of dictionary) and sends data as message to the port'''

    try:
       
        if not isinstance(data, dict):
            raise ValueError("The 'data' argument must be a dictionary")

  
        message = pickle.dumps(data)
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((ip, port))
        client_socket.send(message)
        client_socket.close()


    except Exception as e:
        raise Exception(f"Exception Occured while sending Data: {e}")

def receive_message(ip, port):

    ''' This function takes 2 arguments ip and port to listen for data and return data as a dictionary object'''

    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((ip, port))
        server_socket.listen(1)
        print_blue(f"Listening on '{ip}:{port}'")

        client_socket, client_address = server_socket.accept()
        # print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

        received_data = b""
        
        while True:
            chunk = client_socket.recv(1024)
            if not chunk:
                break
            received_data += chunk

        client_socket.close()
        server_socket.close()

        if received_data:
            data = pickle.loads(received_data)
            return data
        else:
            return None

    except Exception as e:

        raise Exception(f"Exception occured while receiving data: {e}")
     
