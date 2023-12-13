from vidstream import AudioSender
from vidstream import AudioReceiver
import threading, socket

addr=socket.gethostbyname(socket.gethostname())

sender=AudioSender(addr, 9999)
sender_thread=threading.Thread(target=sender.start_stream)

reciever=AudioReceiver(addr, 9999)
reciever_thread=threading.Thread(target=reciever.start_server)

sender_thread.start()
reciever_thread.start()
