import socket
import time



print("-----------Risiko v0.1-------------")
print("-->Server konfigurieren")

spieler = []



def warteAufSpieler():
    while True:
        print("aktuell beigetreten:")
        for s in range(len(spieler)):
            print(spieler[s],"(",s+1,")")
        time.sleep(1)




#netzwerkinitialisierung
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
#print(s.getsockname()[0])






port = input("Geben Sie den Port an, der verwendet werden soll: ")
print("\nServer startet mit Adresse:", s.getsockname()[0], ":", port)
check= input("OK? j/n")

if(check in ["j","J","y","Y","ja","Ja","yes","Yes"]):
    print("Starte Server...")
    warteAufSpieler()
else:
    print("Beende Server")
    s.close()

s.close()