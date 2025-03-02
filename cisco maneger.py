import keyboard
import os
import time
import random
def sleeper(timer):
    time.sleep(timer)

def keabord_presser(key):
    keyboard.press_and_release(key)

def keyboard_write(write):
    keyboard.write(write)

def start_config():
    keabord_presser('enter')
    keyboard_write("ena")
    keabord_presser('enter')
    keyboard_write(enable)
    keabord_presser('enter')
    keyboard_write("conf t")
    keabord_presser('enter')

def exit_R (i):


    while (i) :
        keyboard_write("exit")
        keabord_presser('enter')
        i = i-1

def enter() : 
    keabord_presser('enter')

def start_typing() :
    while(True) :
        p = keyboard.read_key()
        if p == "enter":
            return True
        else :
            return False

def clear_terminal() :
    os.system('cls')

#__________________________________________________________________________________________________________________________________________________________________________________________________

enable = input("enter enable password : ")
clear_terminal()
R_or_S = input("1- Router\n2- Switch\n")
if R_or_S == "1" :
    a = input("""
1- Router ports
2- DHCP
3- default routing
4- ACL
5- RIP          
6- OSPF   
      
            
            
            
            """)
    clear_terminal()
    if a == "1":
        
        name = input("enter interface name : ")
        IP_Mask = input("enter interface IP and mask : ")
        clear_terminal()
        start_typing()
        start_config()
        keyboard_write("interface "+name)
        enter()
        keyboard_write("no shutdown")
        enter()
        keyboard_write("ip addres "+IP_Mask)
        enter()
        exit_R(3)
        print("....^_^....")


    elif a=="2" :
        pool = input("enter DHCP pool number : ")
        N_id = input("enter network ID and mask: ")
        default_router = input("enter default-router : ")
        DNS_server = input("enter DNS-setver : ")
        clear_terminal()
        start_typing()
        start_config()
        keyboard_write("ip dhcp pool "+pool)
        enter()
        keyboard_write("network "+N_id)
        enter()
        keyboard_write("default-router "+default_router)
        enter()
        keyboard_write("dns-server "+DNS_server)   
        enter()
        exit_R(3)
        print("....^_^....")
    elif a == "3" :
        default_IP = input("enter default router IP : ")
        clear_terminal()
        start_typing()
        start_config()
        keyboard_write("ip route 0.0.0.0 0.0.0.0 "+default_IP)
        exit_R(2)
        print("....^_^....")
    elif a == "4" :
        ACL_type = input("type of ACL :\n1- Standard\n2- Extanded\n")
        clear_terminal()
        if ACL_type == "1" :
            ACL_number = 200
            while (ACL_number<=1 or ACL_number>= 100) :
                ACL_number = int(input("enter ACL number : "))
            IP_of_deny_devicre = input("note...if you want to deny network comblitly inter the network ID and while dcarde \nenter IP of device which want to deny : ")
            interface_name = input("enter interface name : ")
            clear_terminal()
            in_out = input("1- in\n2- out\n")
            if in_out == "1":
                in_out = "in"
            else :
                in_out = "out"
            clear_terminal()
            start_typing()
            start_config()
            keyboard_write("access-list "+ str(ACL_number) + " deny "+ IP_of_deny_devicre )
            enter()
            keyboard_write("access-list "+ str(ACL_number) + " permit any ")
            enter()
            keyboard_write("int "+interface_name)
            enter()
            keyboard_write("ip access-group "+str(ACL_number)+" "+in_out)
            enter()
            exit_R(3)
        else : 
            ACL_number = int(input("enter ACL number : "))
            Destination_ip = input("enter Destination ip : ")
            target_ip = input("enter target ip : ")
            interface_N = input("enter interface name : ")
            clear_terminal()
            c = input("1- in\n2- out\n")
            if c==1:
                IN_OUT = "in"
            else :
                IN_OUT = "out"
            clear_terminal()
            protocol = 1
            dale_with = [1,1,1,1,1,1,0,0,1,1,0,0]
            port_number = [80,443,21,25,110,143,53,68,23,22,69,161]
            protocol_num = []
            print("""
    0- Stop
    1- HTTP
    2- HTTPS
    3- FTP
    4- SMTP
    5- POP3
    6- IMAP
    7- DNS
    8- DHCP
    9- Telnet
    10- SSH
    11- TFTP
    12- SNMP 
    """)
            while (protocol !=0) :
                number = int(input())
                protocol_num.append(number-1)
                if number == 0 :
                    break
            clear_terminal()
            start_typing()
            start_config()
            i =0
            while (protocol_num[i] != -1) :
                if dale_with[protocol_num[i]] == 1 :
                    x = "tcp"
                else :
                    x = "udp"
                keyboard_write("access-list "+str(ACL_number)+" deny "+ x + " host "+Destination_ip+" host "+ target_ip+" eq "+str(port_number[protocol_num[i]]) )
                enter()
                i+=1
            keyboard_write("access-list "+str(ACL_number)+" permit ip any any")
            enter()
            keyboard_write("interface "+interface_N)
            enter()
            keyboard_write("ip access-group "+str(ACL_number)+" "+IN_OUT)
            enter()
            exit_R(3)
    elif a == "5" :
        clear_terminal()
        z = input("1- IPv4\n2- IPv6\n")
        if z == "1":
            clear_terminal()

        elif z == "2" :
            clear_terminal()
            random_num = random.randint(1,100)
            interface = input("inter range of interface : ")
            while (start_typing()) :
                
                start_config()
                keyboard_write(f"ipv6 router rip {random_num}")
                enter()
                keyboard_write(f"int range {interface}")
                enter()
                keyboard_write(f"ipv6 rip {random_num} enable")
                enter()
                exit_R(3)
            
            
    elif a == "6" :
        clear_terminal()
        random_num = random.randint(1,100)
        interface1 = input("Enter name of interface 1 : ")
        interface2 = input("Enter name of interface 2 : ")
        while (start_typing()) :
            ran = random.randint(1,192)
            start_config()
            keyboard_write(f"ipv6 router ospf {random_num}")
            enter()
            keyboard_write(f"router-id {ran}.{ran}.{ran}.{ran}")
            enter()
            keyboard_write(f"int range {interface1}")
            enter()
            keyboard_write(f"ipv6 ospf {random_num} area 0")
            enter()
            keyboard_write(f"int {interface2}")
            enter()
            keyboard_write(f"ipv6 ospf {random_num} area 0")
            enter()
            exit_R(3)
            sleeper(1)
        
elif R_or_S == "2" :
    a = input("""
1- Etherchannel
2- DHCP snooping       
            """)
    if a=="1":
        clear_terminal()
        port_range_1 = input("Enter port range of first switch : ")
        port_range_2 = input("Enter port range of secand switch: ")
        rand = random.randint(1,6)
        while start_typing() :
            start_config()
            keyboard_write(f"interface range {port_range_1}")
            enter()
            keyboard_write("switchport mode trunk")
            enter()
            keyboard_write(f"channel-group {rand} mode active")
            enter()
            
            port_range_1 = port_range_2
    elif a == "2" :
        clear_terminal()
        int_trust = input("Enter number of trust interface : ")
        Vlans_number = []
        Vlans_numbers = 1 
        i = 0
        while Vlans_numbers!=0:
            Vlans_numbers = input("Enter VLAN number if you complet it enter 0 : ")
            Vlans_number[i] = Vlans_numbers
            i+=1
        start_typing()
        start_config()
        keyboard_write("ip dhcp snooping ")
        enter()
        keyboard_write("no ip dhcp snooping information option")
        enter()
        for Vlans_numbers in Vlans_number :
            if Vlans_numbers == "0" :
                break
            keyboard_write(f"ip dhcp snooping vlan {Vlans_numbers}")
            enter()
        keyboard_write(f"int {int_trust}")
        enter()
        keyboard_write("ip dhcp snooping trust")
        enter()
        exit_R(3)







    



