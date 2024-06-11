import socket
import threading

def handle_client(client_socket, addr, grid):
    print(f"Connexion acceptée de {addr}")
    while True:
        try:
            # Recevoir les coordonnées de tir
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break

            x, y = map(int, data.split(','))
            print(f"Reçu tir en ({x}, {y})")

            # Vérifier si le tir touche un navire
            if grid[y][x] == 'X':
                client_socket.send("Touché!".encode('utf-8'))
                grid[y][x] = '.'
            else:
                client_socket.send("Manqué!".encode('utf-8'))

        except Exception as e:
            print(f"Erreur: {e}")
            break

    client_socket.close()
