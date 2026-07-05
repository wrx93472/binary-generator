import sys
import socket

sys.path.append('output')
from generated_model import SensorData

def run_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12345))

    # Tworzymy instancję klasy, którą stworzył generator
    obj = SensorData(1, 23.5, 1720177700)
    
    # Serializujemy do formatu binarnego i wysyłamy
    binary_data = obj.serialize()
    client.send(binary_data)
    print("Dane wysłane do serwera.")

    client.close()

if __name__ == "__main__":
    run_client()