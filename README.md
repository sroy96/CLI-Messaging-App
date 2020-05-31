# Chat-CLI-App
A Command line Chat application with one worker/server . Any client with the 
given IP Address and Port number can join. Acknowlwdgement message will be send to the 
sender once all the clients recieve the message broadcasted.
Its the responsibility of the server to maintain the logs of the message with Timestamp,
message body and message Id.
Created with Socket Framework
- createSocket : Creates a Socket using AF_INFET which is an 
address family that is used to designate the type of addresses
 that your socket can communicate with.
  When you create a socket, you have to specify its address family, and
   then you can only use addresses of that type with the socket.

- serverListener : Message sent by the client to connect the worker in orer to 
broadcast the mesage to clients with a wait time of 2048ms.

- server maintains a dictionary of clients in order to broadcast the message one by one
accept the 'DEACTIVE' status which notes the client connection sending the message object.



--------
They grey area I faced -> Since the program is using a single thread. The 
priority queue feature is already handled as the messages will be broadcasted to
clients in single thread.
 


## Usage
Clone repository
```
git clone https://github.com/sroy96/CLI-Chat-App.git
```
Run ```server.py``` with correct parameters, Usage:
```
./server.py
```

```
Afterwards clients can connect to the server using client.py with correct parameters, Usage:
```
./client.py [HOST] [PORT] 

```
Default is again, 127.0.0.1 9001 : i.e Command ->
python3 client.py 127.0.0.1  9001
```


