# FTP using Sockets
===========================


## Setup :

- open the repository and add the file you want to transfer into the folder
- change the **file_name** in _server.py_ to the name of the file you want to transfer
- connect to the same wifi or ethernet
- on the computer acting as the server (Sender), get the local ip address

#### To get your local ip using terminal :

- on Windows

```bash
    ipconfig 
```

- macOS or Linux

```bash
    ipconfig or ip a
```
#### 

- change the **ADDR** on both _server.py_ and _client.py_, to the server's ip address
- Run _server.py_ first
- now run _client.py_
