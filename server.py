import socket
import time
import _thread



print("-----------Risiko v0.1-------------")
print("-->Server konfigurieren")

spieler = []



def warteAufSpieler():
    while True:
        print("aktuell beigetreten:")
        for s in range(len(spieler)):
            print(spieler[s],"(",s+1,")")
        time.sleep(1)

def on_new_client(clientsocket, addr):
    while True:
        msg = clientsocket.recv(1024)
        # do some checks and if msg == someWeirdSignal: break:
        print
        addr, ' >> ', msg
        msg = input('SERVER >> ')
        # Maybe some code to compute the last digit of PI, play game or anything else can go here and when you are done.
        clientsocket.send(msg)
    clientsocket.close()




#netzwerkinitialisierung
stest = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
stest.connect(("8.8.8.8", 80))
#print(s.getsockname()[0])

s=socket.socket()
host=socket.gethostname()






port = input("Geben Sie den Port an, der verwendet werden soll: ")
print("\nServer startet mit Adresse:", stest.getsockname()[0], ":", port)
check= input("OK? j/n")

if(check in ["j","J","y","Y","ja","Ja","yes","Yes"]):
    print("Starte Server...")
    s.bind((host,int(port)))
    s.listen(5)

    #print("Got connection from", addr)
    while True:
        c, addr = s.accept()  # Establish connection with client.
        _thread.start_new_thread(on_new_client, (c, addr))
        # Note it's (addr,) not (addr) because second parameter is a tuple
        # Edit: (c,addr)
        # that's how you pass arguments to functions when creating new threads using thread module.
    s.close()

    #warteAufSpieler()
else:
    print("Beende Server")
    stest.close()

stest.close()