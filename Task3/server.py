# Task 3
# Create live streaming video chat without voice using cv2 module of python
# server.py

import socket, cv2, pickle, struct

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_name  = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print('HOST IP:', host_ip)
print("\n===Creating socket connection===")
port = 9999
socket_address = ('192.168.56.1',port)
print("Socket Created")

print("\t\t\t\n===Creating Socket Bind!!!===")
server_socket.bind(socket_address)
print("Socket Bind Successfully")

print("\t\t\t\n===Starting Listening!!!===")
server_socket.listen(5)
print("LISTENING AT:", socket_address)

print("\t\t\t\n======Socket Accepted!!!=====")
while True:
    client_socket, addr = server_socket.accept()
    print('GOT CONNECTION FROM:', addr)
    if client_socket:
        video = cv2.VideoCapture(0)
        
        while(video.isOpened()):
            img,frame = video.read()
            a = pickle.dumps(frame)
            message = struct.pack("Q", len(a)) + a
            client_socket.sendall(message)
            
            cv2.imshow('TRANSMITTING VIDEO', frame)
            if cv2.waitKey(1) == 13:
                cv2.destroyAllWindows()
                break
    client_socket.close()
    video.release()

                

print("\n======Thank you!!!======")
review_server = input("\nHow much would you like to rate 0-5 : ")
print("\nThank's for reviewing!!!")
print("\t\t\t\n===Task Completed!!!===")
print("\nTask done by : Shashank, Dheeraj, Divyansh, Jai")
