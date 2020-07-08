import socket
from prepare_data import prepare_data

HOST = socket.gethostname()
PORT = 8889

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    with conn:

        data = conn.recv(1024)
        # print("Recieved", data, "from", addr)
        data = data.decode("utf-8")

        data_to_send = prepare_data(data)

        conn.send(f"HTTP/1.1 200 OK\n "
                  f"Content-Length: 1024\n "
                  f"Connection: close\n "
                  f"Content-type: application/json\n\n"
                  f"{data_to_send}".encode("utf-8"))
