import socket
import time
import os


print("""

██████╗  ██████╗ ██████╗ ████████╗    ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
██████╔╝██║   ██║██████╔╝   ██║       ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██╔═══╝ ██║   ██║██╔══██╗   ██║       ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
██║     ╚██████╔╝██║  ██║   ██║       ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
                                                                                                  
""")

#Spaces
print("")
print("")

#Welcome
print("[+]Welcome to port-scanner! coded by c00LAgent")
print("")
print("[+]Github: https://github.com/c00LAgent/")
print("[+]Twitter: https://twitter.com/AgentGeneric")

#IPV4 and Handshake Method

# Handshake Method Menu
print("[*] Select scan type from menu")

#Spaces
print("")
print("")

print("0) TCP Scan")
print("1) Send Ping")

#Spaces
print("")
print("")

print("99) Exit")

#Spaces
print("")
print("")

ScanMethod = int(input("scan> "))

#Initiate Scan
# Enum and Scan

def scanPort(port):
    if s.connect_ex((inputIpHost, port)):
        print("[*] port", port, "is closed")
    else:
        print("[*] port", port, "is open")



#ScanType
if ScanMethod == 0:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Ip and Port
    inputIpHost = input("[+] Enter host ip: ")
    port = int(input("[+] Specify Port:"))


    # Spaces
    print("")
    print("")

    print("[*] Scanning...")

    # Spaces
    print("")
    print("")

    scanPort(port)

elif ScanMethod == 1:

    # Ip and Port
    inputIpHost = input("[+] Enter host ip: ")
    ip = socket.gethostbyname(inputIpHost)

    # Spaces
    print("")
    print("")

    print("[*] Pinging...")

    pingResponse = os.system("ping " + inputIpHost)

    if pingResponse == 0:
        #Spaces
        print("")
        print("")

        print("[*]",inputIpHost,"(",ip,") is up")

    else:
        print("[*]", inputIpHost, (ip), "is down")

elif ScanMethod == 99:
    #Spaces
    print("")
    print("")

    #Exit
    print("[+] Exiting...")
    time.sleep(0.5)
    exit()

else:
    # Spaces
    print("")
    print("")

    print("[+] Please select from Menu")
    time.sleep(0.5)

    #Spaces
    print("")
    print("")

    #Exit
    print("[+] Exiting...")
    time.sleep(0.5)
    exit()













