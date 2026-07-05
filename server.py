import sys
import socket

# Dodajemy folder output do ścieżki, aby Python widział wygenerowany moduł
sys.path.append('output')
from generated_model import SensorData

def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 12345))
    server.listen(1)
    print("Serwer uruchomiony. Czekam na połączenie...")

    conn, addr = server.accept()
    print(f"Połączono z: {addr}")

    # Odbieramy dane binarne (rozmiar bufora 1024 bajty)
    data = conn.recv(1024)
    if data:
        # Wykorzystujemy wygenerowaną metodę deserializacji
        received_obj = SensorData.deserialize(data)
        print(f"Odebrano dane: ID={received_obj.id}, Wartość={received_obj.value}, Czas={received_obj.timestamp}")

    conn.close()

if __name__ == "__main__":
    run_server()