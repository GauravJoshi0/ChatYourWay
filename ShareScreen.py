from vidstream import ScreenShareClient, StreamingServer
import threading, socket

match input("1]. Host\n2]. Join"):
    case 1:
        addr=socket.gethostbyname(socket.gethostname())

        client=ScreenShareClient(addr, 9999)

        client_thread=threading.Thread(target=client.start_stream)

        client_thread.start()

        while input("")!="quit":
            continue

        client.stop_stream()
    case 2:
        addr=socket.gethostbyname(socket.gethostname())

        host=StreamingServer(addr, 9999)

        host_thread=threading.Thread(target=host.start_server)

        host_thread.start()

        while input("")!="quit":
            continue

        host.start_server()