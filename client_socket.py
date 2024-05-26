import socket


class RemoteProx:
    def __init__(self, host='localhost', port=65432):
        self.host = host
        self.port = port

    def start_client(self):
        # Criação do socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Define o endereço e a porta do servidor ao qual o cliente se conectará
        server_address = (self.host, self.port)
        # Conecta-se ao servidor
        client_socket.connect(server_address)

        try:
            # Envia uma mensagem ao servidor
            while True:
                message = str(input("Digite sua Mensagem: "))
                if not (message == "sair"):

                    client_socket.sendall(message.encode())
                    print('Mensagem enviada ao servidor')

                else:
                    client_socket.sendall(message.encode())
                    break

        finally:
            # Fecha o socket
            print("Fechando a Conexão Cliente")
            client_socket.close()


if __name__ == "__main__":
    client = RemoteProx()
    client.start_client()
