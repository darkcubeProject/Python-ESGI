import socket

def main():
    host = '127.0.0.1'
    port = 5555

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    while True:
        try:
            # Saisir les coordonnées de tir séparément
            x = int(input("Entrez la coordonnée X: "))  # Attendre un entier pour X
            y = int(input("Entrez la coordonnée Y: "))  # Attendre un entier pour Y

            # Envoyer les coordonnées au serveur dans le format "X,Y"
            client.send(f"{x},{y}".encode('utf-8'))

            # Recevoir la réponse du serveur
            response = client.recv(1024).decode('utf-8')
            print(f"Réponse du serveur: {response}")

        except Exception as e:
            print(f"Erreur: {e}")
            break

    client.close()
