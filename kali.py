#this is a python tool that allows noobs to easily run commands in kali linux
from os import system
# COLORS #
red = "\033[91;1m"
reset = "\033[0m"
green = "\033[92;1m"
cyan = "\033[96;1m"
yellow = "\033[93;1m"
magenta = "\033[95;1m"
blue = "\033[94;1m"
white = "\033[97;1m"
blink = "\033[5m"

print(magenta+"This tool is writtern and Desinged by Maimo Harris")

print('                    LAZY CYPHER TOOL')
choice=int(input(green+'''[1]:Run Metasploit Tool             [2]:Hack Wifi Networks
[3]:Run Setoolkit                   [4]:Install Airgeddon Tool 
[5]:See and Edit repository         [6]:Run Armitage Tool
[7]:Update and Upgrade kali         [8]:Run Wireshark
[9]:Run Airgeddon tool              [10]:Exit Tool
[11]:Solve WIFI Connection Problem  [12]:Show System IP Address
[13]:Show Devices Connected on Wifi [14]:Run Legion Information Gathering tool
[15]Run Zaproxy Tool                [16]:
Choice::'''))

if choice==1:
    system('msfconsole')
elif choice==2:
    system('sudo wifite')
elif choice==3:
    system('sudo setoolkit')
elif choice==4:
    system('sudo apt install airgeddon')
elif choice==5:
    system('sudo nano /etc/apt/sources.list')
elif choice==6:
    system('sudo armitage')
elif choice==7:
    system('sudo apt update && sudo apt upgrade')
elif choice==8:
    system('sudo wireshark')
elif choice==9:
    system('sudo airgeddon')
elif choice==10:
    system('clear && exit')
elif choice==11:
    system('sudo service NetworkManager stop && sudo service NetworkManager start ')
elif choice==12:
    system('ifconfig')
elif choice==13:
    system('sudo netdiscover -i wlan0')
elif choice==14:
    system('sudo legion')
elif choice==15:
    system('Run Zaproxy tool')