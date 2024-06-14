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

def main():
    host = '0.0.0.0'
    port = 5555

    # Initialiser la grille de jeu (5x5 pour simplification)
    grid = [['.' for _ in range(10)] for _ in range(10)]
    grid[2][2] = 'X'  # Un navire est placé en (2, 2)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(2)
    print(f"Serveur en écoute sur {host}:{port}")

    while True:
        client_socket, addr = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, addr, grid))
        client_handler.start()

if __name__ == "__main__":
    main()
