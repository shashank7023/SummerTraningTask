# Task 3
# Create live streaming video chat without voice using cv2 module of python
# client.py

import socket, cv2, pickle, struct

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# Getting host ip address
host_ip = input("Enter the ip address of Server : ")
# port address of host
port = 9999
print("\n===Creating socket connection===")
print("======Socket Created======")
print("\t\t\t\n===Waiting for host to accept the socket connection!!!===")

client_socket.connect((host_ip,port))
data = b""
payload_size = struct.calcsize("Q")
print("======Socket Accepted======")
print("\t\t\t\n===Ready for video chat!!!===")

while True:
    while len(data) < payload_size:
        packet = client_socket.recv(4*1024) # 4K
        if not packet: break
        data+=packet
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("Q", packed_msg_size)[0]
    
    while len(data) < msg_size:
        data += client_socket.recv(4*1024)
    frame_data = data[:msg_size]
    data  = data[msg_size:]
    frame = pickle.loads(frame_data)
    cv2.imshow("RECEIVING VIDEO", frame)
    # key = cv2.waitKey(1)
    if cv2.waitKey(1) == 13:
        cv2.destroyAllWindows()
        break

client_socket.close()


print("\n======Thank you!!!======")
review_client = input("\nHow much would you like to rate 0-5 : ")
print("\nThank's for reviewing!!!")
print("\t\t\t\n===Task Completed!!!===")
print("\nTask done by : Shashank, Dheeraj, Divyansh, Jai")
